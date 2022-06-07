import os
import json
import dlib
import skvideo.io
import cv2
from subprocess import call
import makeDir

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

with open ("./videos.json","r") as loadJson:
    LOAD = json.load(loadJson)
    for key, value in LOAD.items():
        os.makedirs("./data/{}/face_video".format(key))
       
        # 폴더 만들기
        # 이미지 경로 불러오기
        image_path = makeDir. makeImageDir(key)
        print(image_path)

        for mp4_path in image_path:
            print("this Count session = " + mp4_path)
            v_cap = cv2.VideoCapture(mp4_path)

            if v_cap.isOpened():
                while True: #무한루프
                    success, image = v_cap.read()  # BGR
                    print("OK")
                    try:
                        if success and int(v_cap.get(1)) == 1:
                        #if success :
                            boxes = detector(image)
                            box = boxes[0]
                            print("box: ", box)
                            face = image[box.top():box.bottom(), box.left():box.right()]
                            #print(face)
                            PATH = mp4_path.replace('video', 'face_video')
                            #cv2.imwrite(os.path.join(PATH, '%d.png' % v_cap.get(1)), face)
                            
                            # 너비 , 높이, 수평위치, 수직위치
                            call('ffmpeg -i {} -vf "crop={}:{}:{}:{}" {}'.format(mp4_path, 
                                                                                box.bottom()-box.top(),
                                                                                box.right()-box.left(),
                                                                                box.left(),
                                                                                box.top(),
                                                                                PATH), shell =True)
                        else:
                            break
                            #얼굴 못찾는 영상 넘기기
                    except IndexError:
                        print("error")


'''
영상 제로 패딩 추가하기
프레임별로 추출한 이미지는 넘파이 배열로 이루어져있음
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.unit8) #컬러
img = np.zeros((512, 512), np.unit8) #흑백

cv2.imshow('img',img)

cv2.waitKey()
'''
