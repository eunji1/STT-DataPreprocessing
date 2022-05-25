from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())

print(buckets)