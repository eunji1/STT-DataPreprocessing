import os
import json


# with open ("./videos.json","r") as loadJson:
#     LOAD = json.load(loadJson)
#     for key, value in LOAD.items():
#         result.append(key) 

def makeImageDir(result)
    for key in result:
        with open('/home/SEJ/STT-DataPreprocessing/STT/wavs/' + key + '.json') as f:
            data = json.load(f)
        for count in range(len(data)):
            file_names = os.listdir('./data/{}/{}_{}/video'.format(key, key, count))
            for label in file_names:
                t_label=label[:-4]
                os.makedirs("./data/{}/{}_{}/image/{}".format(key, key, count, t_label)) #label