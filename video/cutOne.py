import getVideos
import json
from subprocess import call
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

result = getVideos.test("./videos.json")
#['001','002','003']

# STT 한단어는 자르기
#WordJson은 어절단위로 자른 영상 정답 라벨을 모은 제이슨파일
WordJson = []

for key in result:
	os.makedirs("./data/{}/video".format(key))
	os.makedirs("./data/{}/align".format(key))
	# data/001/video/001_1_001.avi
	# data/001/image/001_1_001/1.png
	VideoNameJson = {"VideoName" : key, "words":[]}
	WordJson.append(VideoNameJson)
	ListJson = []
	with open('/home/SEJ/STT-DataPreprocessing/STT/wavs/' + key + '.json') as f:
		data = json.load(f)

	for count in range(len(data)):
		dictTime = data[count]['words']
		num = 0
		for row in dictTime:
			# end_time, start_time, word를 WordTimeList안에 따로 담기  
			WordTimeList = []
			for stt in row.values():    
				WordTimeList.append(stt)
				num += 1
				#print(num/3)
				#print(WordTimeList)

			# 길이가 한단어는 삭제
			if len(WordTimeList[2]) > 1:
				Num = str(int(num/3)).zfill(2)
				video_name = '{}_{}_{}'.format(key, count, Num)
				WordListJson = {"fileName": video_name, "word": WordTimeList[2]}
				ListJson.append(WordListJson)

				# 총1.7초
				ffmpeg_extract_subclip("./avi/{}.avi".format(key), 
										WordTimeList[1]-0.5, 
										WordTimeList[1]+1.2, 
										targetname="./data/{}/video/{}.avi".format(key, video_name))

				#align.txt 만들기
				txt = open("./data/{}/align/{}.txt".format(key, video_name), 'a')
				txt.write("word: {} \nstarttime: {} \nendtime: {} \nduration: 1.7".format(WordTimeList[2], WordTimeList[1]-0.5, WordTimeList[1]+1.2))
				txt.close
		VideoNameJson["words"] = ListJson	

with open('WordJson.json', 'w') as f:
	json.dump(WordJson, f, indent=4, ensure_ascii=False)