import getVideos
import os
import json
import dlib
import skvideo.io
import cv2


result = getVideos.test("./videos.json")

# 한 어절 영상당 30장 맞추어 output 맞추기
#약 1.6초 영상 42개 나옴

## face detector와 landmark predictor 정의
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
# data/001/001_001/video/001_001안녕하세요.avi
# data/001/001_001/image/1.png

## 비디오 읽어오기
#json 경로
for i in result:
    with open('/home/sej/data/STT/wavs/' + i + '.json') as f:
        data = json.load(f)
        for count in range(len(data)):
            file_names = os.listdir('./data/{}/{}_{}/video'.format(i, i, count))
            for label in file_names:
                os.makedirs("./data/{}/{}_{}/image/{}".format(i, i, count, label))
                mp4_path = '/data/{}/{}_{}/video/'+label
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
                                l = rect.left()
                                t = rect.top()
                                b = rect.bottom()
                                r = rect.right()
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
                                #cv2.imshow('frame', resized)
                                img_path = "./data/{}/{}_{}/image/".format(i, i, count)
                                cv2.imwrite(os.path.join(img_path, '%d.png' % v_cap.get(1)), resized)
                                print("Frame Captured: %d" % v_cap.get(1))
                                #if cv2.waitKey(1) & 0xFF == ord('q'):
                                #break
                            # cv2.destroyAllWindows()
                else :
                    break