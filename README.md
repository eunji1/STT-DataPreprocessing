# STT-DataPreprocessing

## TODO

###STT
- [x] 영상다운받기
- [x] 영상 GCS에 올리기
- [x] 영상 JSON 형태로 STT 추출
- [x] 503에러 해결
	- [x] json파일 경로 './STT/wavs/'

###Video
- [x] 영상 단어(어절)에 맞추어 자르기
- [x] 입술 크롭한 데이터 폴더명 지정하기
- [ ] 데이터 덮어쓰기 & 삭제코드 만들기
- [ ] 크롭하고나서 생각해 볼것! 데이터고르기
	- [ ] 너무 짧은 영상 삭제 -> time 기준? word 기준?
	- [ ] 한명이 말하고 있지 않은 영상 삭제 ->입술을 찾지 못할 때
	- [ ] 필요없는 단어 삭제 -> 빈도수를 알아보고 적게 나온 단어 삭제 


## 문제점

- 한 어절 영상당 규격 맞춰주기
	- 시간을 맞추기는 어려울 듯 프레임으로 자른 이미지를 몇개로 제한
	- 작은것은 지우고 큰것은 랜덤으로 삭제



## 준비물
- `youtube` 영상 링크를 모아둔 `Json` 파일

```json
// -ex

{
	"파일이름":"링크",
	"002":"https://www.youtube.com/watch?v=bQF4umz6YCE&t=11s"

}
```


## 사용법

```py
python3 auto.py

python3 cutVideo.py
python3 cropMouth.py
```

## 사용된 Library

```py
backports.zoneinfo==0.2.1
beautifulsoup4==4.11.1
cachetools==5.1.0
certifi==2022.5.18.1
charset-normalizer==2.0.12
docopt==0.6.2
ffmpeg-python==0.2.0
future==0.18.2
google-api-core==2.8.0
google-auth==2.6.6
google-cloud-core==2.3.0
google-cloud-speech==2.14.0
google-cloud-storage==2.3.0
google-crc32c==1.3.0
google-resumable-media==2.3.3
googleapis-common-protos==1.56.1
grpcio==1.46.3
grpcio-status==1.46.3
idna==3.3
Js2Py==0.71
packaging==21.3
pipwin==0.5.2
proto-plus==1.20.4
protobuf==3.19.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pydub==0.25.1
pyjsparser==2.7.1
pyparsing==3.0.9
PyPrind==2.11.3
pySmartDL==1.3.4
pytube==12.1.0
pytz-deprecation-shim==0.1.0.post0
requests==2.27.1
rsa==4.8
six==1.16.0
soupsieve==2.3.2.post1
SpeechRecognition==3.8.1
tzdata==2022.1
tzlocal==4.2
urllib3==1.26.9

```