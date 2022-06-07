# STT-DataPreprocessing

## TODO

###STT
- [x] 영상다운받기
- [x] 영상 GCS에 올리기
- [x] 영상 JSON 형태로 STT 추출

###Video
- [x] 영상 단어(어절)에 맞추어 자르기
- [x] 입술 크롭한 데이터 폴더명 지정하기


## 문제점

- 파일/ 폴더명이 한글일 경우 잘 불러오지 못하는 문제점이 있다.

- 한 어절 영상당 규격 맞춰주기
	- 시간을 맞추기는 어려울 듯 프레임을 일정하게 맞추기


## 준비물
- `youtube` 영상 링크를 모아둔 `Json` 파일
- 파일 이름 저장 생각해보기(영어 or 숫자)
- 링크 중복 데이터가 있을 경우 삭제하기
- 한번에 많은 데이터 돌리지 말아야 할것! 중간에 끊길 경우 첨부터 다시..

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
dbus-python==1.2.16
decorator==4.4.2
distro-info==1.0
dlib==19.24.0
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
imageio==2.19.2
imageio-ffmpeg==0.4.7
Js2Py==0.71
moviepy==1.0.3
numpy==1.22.4
opencv-python==4.5.5.64
packaging==21.3
Pillow==9.1.1
pipwin==0.5.2
proglog==0.1.10
proto-plus==1.20.4
protobuf==3.19.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pydub==0.25.1
pyjsparser==2.7.1
pyparsing==3.0.9
PyPrind==2.11.3
pySmartDL==1.3.4
python-apt==2.2.1
pytube==12.1.0
pytz-deprecation-shim==0.1.0.post0
requests==2.27.1
rsa==4.8
scikit-video==1.1.11
scipy==1.8.1
six==1.16.0
sk-video==1.1.10
soupsieve==2.3.2.post1
SpeechRecognition==3.8.1
tqdm==4.64.0
tzdata==2022.1
tzlocal==4.2
unattended-upgrades==0.1
urllib3==1.26.9


```