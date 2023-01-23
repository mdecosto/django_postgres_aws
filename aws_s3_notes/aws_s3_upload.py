import boto3

s3_resource = boto3.resource('s3')

file_name = '65c792secondfile.txt'
bucket_name = 'firstpythonbucket905cddd4-c102-4b8e-a561-2a313bcc689b'

s3_resource.meta.client.upload_file(
    Filename=file_name, 
    Bucket=bucket_name,
    Key=file_name
  )