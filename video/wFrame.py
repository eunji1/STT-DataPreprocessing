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
        # 폴더 만들기
        # 이미지 경로 불러오기
        image_path = makeDir. makeImageDir(key)
        print(image_path)

        for mp4_path in image_path:
            print("this Count session = " + mp4_path)
            v_cap = cv2.VideoCapture(mp4_path)
            n_frames = int(v_cap.get(7))
            print(n_frames)
            # 영상별 프레임 수 알아보기