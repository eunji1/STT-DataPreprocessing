# STT-DataPreprocessing

## TODO
- [x] 영상다운받기
- [x] 영상 GCS에 올리기
- [x] 영상 JSON 형태로 STT 추출
- [x] 영상 단어에 맞추어 자르기
- [ ] 미정

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