import os
import json


result = []
with open ("./videos.json","r") as loadJson:
    LOAD = json.load(loadJson)
    for key, value in LOAD.items():
        result.append(key) 

# 한 어절 영상당 30장 맞추어 output 맞추기
#약 1.6초 영상 42개 나옴

## 비디오 읽어오기
# json 경로
    for key in result:
        with open('/home/SEJ/STT-DataPreprocessing/STT/wavs/' + key + '.json') as f:
            data = json.load(f)
        for count in range(len(data)):
            file_names = os.listdir('./data/{}/{}_{}/video'.format(key, key, count))
            for label in file_names:
                t_label=label[:-4]
                #os.makedirs("./data/{}/{}_{}/image/{}".format(key, key, count, t_label)) #label
                mp4_path = './data/{}/{}_{}/video/'.format(key, key, count)+label
                print(mp4_path)