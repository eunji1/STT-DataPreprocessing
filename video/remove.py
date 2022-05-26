#data/001/001_001/video/001_001_안녕하세요.avi
#data/001/001_001/image/안녕하세요/1.png

import os

dir_path = ["video/avi", "video/data"]

for i in dir_path:
    if os.path.exists(i):
        os.rmdir(i)