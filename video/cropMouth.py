import os
import json
import dlib
import skvideo.io
import cv2
import makeDir
## face detector와 landmark predictor 정의
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
# data/001/001_1/video/001_001안녕하세요.avi
# data/001/001_1/image/001_001안녕하세요/1.png

result = []
with open ("./videos.json","r") as loadJson:
    LOAD = json.load(loadJson)
    for key, value in LOAD.items():
        result.append(key) 

# 한 어절 영상당 30장 맞추어 output 맞추기

## 비디오 읽어오기
# json 경로
for key in result:
    with open('/home/SEJ/STT-DataPreprocessing/STT/wavs/' + key + '.json') as f:
        data = json.load(f)
    for count in range(len(data)):
        file_names = os.listdir('./data/{}/{}_{}/video'.format(key, key, count))
        for label in file_names:
            t_label=label[:-4]
            os.makedirs("./data/{}/{}_{}/image/{}".format(key, key, count, t_label)) #label
            mp4_path = './data/{}/{}_{}/video/'.format(key, key, count)+label
            v_cap = cv2.VideoCapture(mp4_path)
                
            if v_cap.isOpened():
                while True:
                    success, image = v_cap.read()  # BGR
                    if success:
                    # if success and int(v_cap.get(1)) % 5 == 0:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #흑백
                        # img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        resized = cv2.resize(image, dsize=(1600, 1200), interpolation=cv2.INTER_LINEAR)  # (1920, 1080)
                        rects = detector(resized, 1)
                        for i, rect in enumerate(rects):
                            shape = predictor(resized, rect)
                            left_x, left_y, right_x, right_y = 0, 0, 0, 0

                            for j in range(68):  # Face Detection
                            #for j in range(48, 68):  # Mouth Detection
                                x, y = shape.part(j).x, shape.part(j).y
                            left_x = shape.part(4).x
                            left_y = shape.part(30).y
                            right_x = shape.part(13).x
                            right_y = shape.part(8).y
                            resized = resized[left_y:right_y, left_x:right_x]  # [높이(행), 너비(열)]
                            img_path = "./data/{}/{}_{}/image/{}".format(key, key, count, t_label)
                            cv2.imwrite(os.path.join(img_path, '%d.png' % v_cap.get(1)), resized)
                            #./data/001/001_0/image/001_01안녕하세요
                            print("Frame Captured: %d" % v_cap.get(1))
                            #if cv2.waitKey(1) & 0xFF == ord('q'):
                            #break
                        # cv2.destroyAllWindows()
                    else :
                        break