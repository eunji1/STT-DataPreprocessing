#data/001/001_001/video/001_001_안녕하세요.avi
#data/001/001_001/image/안녕하세요/1.png

import shutil
import os
# 폴더 안에 파일이 있어도 삭제
# ./video/data/*/*/image
dir_path = ["./avi", "./data"]
for i in dir_path:
    shutil.rmtree(i)
    os.mkdir(i)

# dir_path = ["001", "002"]
# for i in dir_path:
#     shutil.rmtree('/home/SEJ/STT-DataPreprocessing/video/data/{}/image'.format(i))
    #shutil.rmtree('/home/SEJ/STT-DataPreprocessing/video/data/002/image'.format(i))
