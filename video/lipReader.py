"""
Given a input video (.mp4), outputs the probabilities of the k most
plausible words.
Also outputs a .avi file that shows the input of the neural network and
a summary bar graph
"""
# https://github.com/khazit/Lip2Word/blob/master/lipReader.py

import os
import cv2
import sys
import argparse
import face_recognition
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from model.inception import inception_model_fn

tf.logging.set_verbosity(tf.logging.FATAL)
plt.style.use(['dark_background', 'presentation.mplstyle'])

# 영상 29프레임으로 맞추기 // 패딩

def videoToArray(path) :
    """
    Capture every frame of a .mp4 file and save them to
    a 3D numpy array.
    Args :
        - path: path to the .mp4 file
    Return :
        - 4D numpy array
    """
    vidObj = cv2.VideoCapture(path)

    # Some useful info about the video
    width = int(vidObj.get(3))
    height = int(vidObj.get(4))
    fps = int(vidObj.get(5))
    n_frames = int(vidObj.get(7))
    print("Video info : {}x{}, {} frames".format(
        height,
        width,
        n_frames))
    # Create the numpy array that will host all the frames
    # Could use np.append later in the loop but this is
    # more efficient
    video = np.zeros((height, width, n_frames))
    video = video.astype(np.uint8)

    # Iterate over every frame of the video
    i = 0
    while True :
        # Capture one frame
        success, frame = vidObj.read()
        if not success :
            break;
        else :
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Save to one 4D numpy array
            video[:, :, i] = frame
            i += 1
    return video, n_frames, fps

def frameAdjust(video):
    """
    Select a fixed number of frames from the input video
    Args :
        - 3D numpy array
    Returns :
        - Adjusted numpy array
    """
    target = 29
    n_frames = video.shape[2]
    if target == n_frames :
        print("Perfect number of frames !")
        return video
    else :
        if n_frames > target :
            # If number of frames is more than 29, we select
            # 29 evenly distributed frames
            print("Adjusting number of frames")
            idx = np.linspace(0, n_frames-1, 29) #1차원 배열만들기 : 0~ 총프레임 수까지 29개 일정한 간격으로 만들기
            idx = np.around(idx, 0).astype(np.int32) #반올림
            print("Indexes of the selected frames : \n{}".format(idx))
            return video[:, :, idx]
        else :
            # If number of frames is less than 29, duplicate last
            # frame at the end of the video
            output_video = np.zeros((video.shape[0], video.shape[1], 29)).astype(np.uint8)
            output_video[:, :, :n_frames] = video
            for i in range(target-n_frames+1) :
                output_video[:, :, i+n_frames-1] = output_video[:, :, n_frames-1] #복제
            return output_video


def reshapeAndConvert(video) :
    """
    Reshape the video to a 4D array before feeding it to the model function
    Also apply normalization to go from [0-255] to [0-1]
    Args :
        - 3D numpy array
    Returns :
        - 4D numpy array
    """
    size = video.shape[0]
    n_frames = video.shape[2]
    video = np.reshape(video, (1, size, size, n_frames)).astype(np.float32)
    return video / 255.0

def create_dict_word_list(path) :
    '''
    Create a dict used to transfrom labels from int to str
    Args :
        - path : Path to the word list
    Return :
        - Python dictionnary {Word : Label}
    '''
    count = 0
    my_dict = dict()
    with open(path+'word_list.txt', 'r') as f:
        for line in f:
            my_dict.update({count : line[:-1]})
            count += 1
    return my_dict

# Debugging function
# 일련의 프레임을 동영상으로 저장
def _write_video(video, path, fps) :
    #저장할 파일이름, fourcc, 초당 프레임수, 프레임크기
    writer = cv2.VideoWriter(
        path+".avi",
        cv2.VideoWriter_fourcc(*"XVID"),
        fps,
        (256,256)
        isColor=None
    )
    video = video * 255
    for i in range(29) :
        writer.write(
            cv2.resize(
                cv2.cvtColor(
                    video[0, :, :, i].astype('uint8'),
                    cv2.COLOR_GRAY2BGR
                ),
                dsize=(256, 256),
                interpolation=cv2.INTER_LINEAR
            )
        )
    writer.release()


parser = argparse.ArgumentParser()
parser.add_argument(
    '--file',
    default=None,
    help="Name/path of the video file"
)
parser.add_argument(
    '--checkpoint_path',
    default=None,
    help="Path to the checkpoint file"
)
parser.add_argument(
    '--output',
    default=".",
    help="Name of the ouput file"
)
parser.add_argument(
    '--k',
    default="10",
    help="Show top-k predictions"
)


if __name__ == '__main__':
    # Useful stuff
    args = parser.parse_args()
    assert os.path.isfile(args.file), "Video file not found"
    im_size = 64
    n_frames = 29
    params = {"num_classes": 500}
    word_dict = create_dict_word_list("data/")

    # Preprocessing
    print("Reading frames from {}".format(args.file))
    video, n_frames_original, fps = videoToArray(args.file)
    video = frameAdjust(video)
    print("Cropping video around the speaker's mouth (may take time)")
    video = mouthCrop(video)
    video = reshapeAndConvert(video)
    # Used for debugging, not important :
    # fps_output aligns the input video used by the model with the original video
    fps_output = int(fps * (n_frames / n_frames_original)) 
    _write_video(video, args.output, fps_output)

    # Create the classifier
    print("Creating classifier from {}".format(args.checkpoint_path))
    classifier = tf.estimator.Estimator(
        model_fn=inception_model_fn,
        params=params,
        model_dir=args.checkpoint_path
    )
    # Inference time !
    print("Computing predictions")
    predictions = classifier.predict(
        input_fn=tf.estimator.inputs.numpy_input_fn(
            {"x": video},
            batch_size=1,
            shuffle=False
        )
    )

    # Print predictions
    predictions = list(predictions)[0]
    predicted_class = predictions["classes"]
    top_k_classes = (-predictions["probabilities"]).argsort()[:int(args.k)]
    predicted_words = list()
    print("Predictions :")
    for label in top_k_classes :
        predicted_words.append(word_dict[label])
        print("* {} : {} %".format(
            word_dict[label],
            predictions["probabilities"][label]*100
        ))

    # Draw plot and write a .png file
    print("Rendering prediction plot to {}.png".format(args.output))
    idx = [3*i for i in range(int(args.k))]
    plt.figure(figsize=(int(args.k)//2+5, 5))
    plt.bar(
        x=idx,
        height=predictions["probabilities"][top_k_classes],
        color="goldenrod"
    )
    plt.xlabel('Words')
    plt.ylabel('Probabilities')
    plt.title("Most plausible words".format(args.k))
    plt.xticks(idx, predicted_words)
    plt.savefig(
        args.output+".png",
        transparent=False,
        bbox_inches="tight"
    )

    print("Done.")