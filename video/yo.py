#data/001/001_001/video/001_001_안녕하세요.avi
#data/001/001_001/image/안녕하세요/1.png

import shutil
import os
# 폴더 안에 파일이 있어도 삭제
# ./video/data/*/*/image
mostWord = ['여러분', '안녕하십니까', '코로나', '오늘', '확진자', '이번', '다시']
for i in mostWord:
    shutil.rmtree('./MostWord/{}'.format(i))
    #os.mkdir('./test')

# dir_path = ["001", "002"]
# for i in dir_path:
#     shutil.rmtree('/home/SEJ/STT-DataPreprocessing/video/data/{}/image'.format(i))
    #shutil.rmtree('/home/SEJ/STT-DataPreprocessing/video/data/002/image'.format(i))