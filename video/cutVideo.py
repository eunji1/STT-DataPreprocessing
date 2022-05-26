import getVideos
import json
from subprocess import call
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

result = getVideos.test("./videos.json")
#['001','002','003']

#WordJson은 어절단위로 자른 영상 정답 라벨을 모은 제이슨파일
WordJson = []

for key in result:
	VideoNameJson = {"VideoName" : key, "words":[]}
	WordJson.append(VideoNameJson)
	ListJson = []
	with open('/home/SEJ/STT-DataPreprocessing/STT/wavs/' + key + '.json') as f:
		data = json.load(f)

	for count in range(len(data)):
		dictTime = data[count]['words']
		num = 0
		os.makedirs("./data/{}/{}_{}/video".format(key, key, count))
		
		for row in dictTime:
			# end_time, start_time, word를 WordTimeList안에 따로 담기  
			WordTimeList = []
			for stt in row.values():    
				WordTimeList.append(stt)
				num += 1
				#print(num/3)
				#print(WordTimeList)
			Num = str(int(num/3)).zfill(2)
			#앞뒤로 0.2초 패딩
			video_name = '{}_{}_{}'.format(key, count, Num)
			#WordListJson[video_name] = WordTimeList[2]
			WordListJson = {"fileName": video_name, "word": WordTimeList[2]}
			ListJson.append(WordListJson)

			ffmpeg_extract_subclip("./avi/{}.avi".format(key), 
									WordTimeList[1]-0.2, 
									WordTimeList[0]+0.2, 
									targetname="./data/{}/{}_{}/video/{}_{}_{}.avi".format(key, key, count, key, count, Num))
		
		VideoNameJson["words"] = ListJson	

with open('WordJson.json', 'w') as f:
	json.dump(WordJson, f, indent=4, ensure_ascii=False)
									# data/001/001_1/video/001_001안녕하세요.avi