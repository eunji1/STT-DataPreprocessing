import os
import json
import shutil

result=[]
with open ("./videos.json","r") as loadJson:
	LOAD = json.load(loadJson)
for key, value in LOAD.items():
	result.append(key)

#mostWord = ['여러분', '안녕하십니까', '코로나', '오늘', '확진자', '이번', '다시']
mostWord = ['안녕하십니까', '안녕']
for file_name in mostWord:
    #os.makedirs("./MostWord/{}/video".format(file_name)) #폴더 이름 생각
    os.makedirs("./MostWord/{}/videoA".format(file_name))    
for key in result:
    txt_names = os.listdir('./data/{}/align/'.format(key))
    path ='./data/{}/align/'.format(key)

    for word in txt_names:
        txt_path = path + word
        wordList = open(txt_path, 'r')
        line = wordList.readline()
        #print(line[6:-2])
# txt -> avi
        try:
            if line[6:-2] in mostWord:
                txt = "파일명: " + word + line
                wordListtxt = open("word_list.txt", 'w')
                wordListtxt.write(txt)
                print(txt)
                #avi_path = txt_path.replace('align', 'face_video').replace('txt', 'avi')
                avi_path = txt_path.replace('align', 'video').replace('txt', 'avi') #face_vide - video ,video - videoA
                #shutil.copy(avi_path, "./MostWord/{}/video/{}.avi".format(line[6:-2], word[:-4]))
                shutil.copy(avi_path, "./MostWord/{}/videoA/{}.avi".format(line[6:-2], word[:-4]))
            wordListtxt.close()
        except:
            print('error')