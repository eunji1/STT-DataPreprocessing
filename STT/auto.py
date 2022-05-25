import getAudioes
import sendToGCS
import sttJson
import json
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

bucket_name = "example_baker"

# wav파일 가져오기
result = getAudioes.test("./videos.json")

for i in result:
	destination_blob_name = source_file_name =  i
    # wav 파일 GCS로 옮기기
	sendToGCS. upload_blob(bucket_name ,source_file_name,destination_blob_name ) 
    # STT변환
	jsonName = sttJson.transcribe_gcs_with_word_time_offsets('gs://example_baker/'+i)

    # json파일 GCS로 옮기기
    # 굳이 옮겨야 할까?
    
	jsonFileName = i[:-4]+'.json'
	with open('./wavx/'+jsonFileName, 'w') as f:
		json.dump(jsonName, f, indent=4, ensure_ascii=False)
	destinationJsonName = './One/' + jsonFileName 

	sendToGCS. upload_blob(bucket_name ,jsonFileName, destinationJsonName )
