import getVideos
import json
from subprocess import call
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


result = getVideos.test("./videos.json")
#['001','002','003']

for i in result:
	#json파일 어디 저장된지 알아야함
	with open(i + '.json') as f:
		data = json.load(f)

		for count in range(len(data)):
			dictTime = data[count]['words']
			num = 0
			for row in dictTime:
				WordTimeList = []
    			# end_time, start_time, word를 WordTimeList안에 따로 담기    
				for stt in row.values():    
					WordTimeList.append(stt)
					num += 1
    				#print(num/3)
    				#print(WordTimeList)
					#앞뒤로 0.5초 패딩
					ffmpeg_extract_subclip("./avi/{}.avi".format(i), 
										WordTimeList[1]-0.5, 
										WordTimeList[0]+0.5, 
										targetname="./data/{}/{}_{}/{}_{}{}.avi".format(i, i, count, i, count, int(num/3).zfil(3), WordTimeList[2]))