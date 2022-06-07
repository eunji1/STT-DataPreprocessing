import os
import json
import dlib
import skvideo.io
import cv2
from subprocess import call
import makeDir

# 지정한 폴더 영상별 프레임 수 알아보기
key='and'
PATH = './MostWord/{}/video/'.format(key)
file_names = os.listdir(PATH)

for mp4_path in file_names:
    print("this Count session = " + mp4_path)
    v_cap = cv2.VideoCapture(PATH + mp4_path)
    n_frames = int(v_cap.get(7))
    print(n_frames)
