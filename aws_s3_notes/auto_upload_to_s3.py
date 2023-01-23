from sh import pg_dump
import boto3
from datetime import datetime
import os


date_time = datetime.now().strftime("y%Ym%bd%dh%Hm%Ms%S%z")
file_name = f"demo_1_{date_time}.sql".lower()

# download db from rds
pg_dump(host='database-1.cauege7tqa7u.ap-northeast-1.rds.amazonaws.com', username='awspostgres', dbname='demo_1', file=file_name)

# upload db to s3
s3_resource = boto3.resource('s3')

bucket_name = 'demo-1-d2023-jan-18'

s3_resource.meta.client.upload_file(
    Filename=file_name, 
    Bucket=bucket_name,
    Key=file_name
  )

# delete dowloaded db local

os.remove(file_name) 