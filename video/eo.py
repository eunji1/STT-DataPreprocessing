import os
import json
import dlib
import skvideo.io
import cv2
## face detector와 landmark predictor 정의

# data/001/001_1/video/001_001안녕하세요.avi
# data/001/001_1/video/001_001안녕하세요.avi
# data/001/001_001/image/1.png

result = []
with open ("/home/sej/data/STT/videos.json","r") as loadJson:
    LOAD = json.load(loadJson)
    for key, value in LOAD.items():
        result.append(key) 

    for key in result:
        with open('/home/sej/data/STT/wavs/' + key + '.json') as f:
            data = json.load(f)
        for count in range(len(data)):
            print(count)
            file_names = os.listdir('./data/{}/{}_{}/video'.format(key, key, count))
            #for label in file_names:
