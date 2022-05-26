import getVideos
import json
from subprocess import call
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

result = getVideos.test("/home/sej/data/STT/videos.json")
#['001','002','003']

for key in result:
	with open('/home/sej/data/STT/wavs/' + key + '.json') as f:
		data = json.load(f)

	for count in range(len(data)):
		dictTime = data[count]['words']
		num = 0
		os.makedirs("./data/{}/{}_{}/video".format(key, key, count))
		for row in dictTime:
			WordTimeList = []
			# end_time, start_time, word를 WordTimeList안에 따로 담기    
			for stt in row.values():    
				WordTimeList.append(stt)
				num += 1
				#print(num/3)
				#print(WordTimeList)
			Num = str(int(num/3)).zfill(2)
			#앞뒤로 0.2초 패딩
			ffmpeg_extract_subclip("./avi/{}.avi".format(key), 
									WordTimeList[1]-0.2, 
									WordTimeList[0]+0.2, 
									targetname="./data/{}/{}_{}/video/{}_{}{}.avi".format(key, key, count, key, Num, WordTimeList[2]))
									# data/001/001_1/video/001_001안녕하세요.avi