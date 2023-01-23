import boto3

# s3_client = boto3.client('s3')

# s3_resource = boto3.resource('s3')

# s3_resource.meta.client.generate_presigned_url()

# create bucket with unique id

import uuid

def create_bucket_name(bucket_prefix):
  return ''.join([bucket_prefix, str(uuid.uuid4())])

# print(create_bucket_name('test_name'))


def create_bucket(bucket_prefix, s3_connection):
  session = boto3.session.Session()
  current_region = session.region_name
  bucket_name = create_bucket_name(bucket_prefix)
  if current_region == 'us-east-1':
    bucket_response = s3_connection.create_bucket(
      Bucket=bucket_name
    )
  else:      
    bucket_response = s3_connection.create_bucket(
      Bucket=bucket_name,
      CreateBucketConfiguration={
        'LocationConstraint': current_region
      }
    )
  print(bucket_name, current_region)
  return bucket_name, bucket_response

def create_temp_file(size, file_name, file_content):
  random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
  with open(random_file_name, 'w') as f:
    f.write(str(file_content) * size)
  return random_file_name


s3_resource = boto3.resource('s3')

# create bucket name and file name
first_bucket_name, first_response = create_bucket(
  bucket_prefix='123pythonbucket',
  s3_connection=s3_resource.meta.client)
first_file_name = create_temp_file(300, '123file.txt', 'e')

first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(bucket_name=first_bucket_name, key=first_file_name)

first_bucket_again = first_object.Bucket()
first_object_again = first_bucket.Object(first_file_name)


# uploading - Object Instance Version

# s3_resource.Object(
#     first_bucket_name, 
#     first_file_name
#   ).upload_file(Filename=first_file_name)

# # uploading - Bucket Instance Version

# s3_resource.Bucket(first_bucket_name).upload_file(
#     Filename=first_file_name, 
#     Key=first_file_name
#   )

# # uploading - Client Version

s3_resource.meta.client.upload_file(
    Filename=first_file_name, 
    Bucket=first_bucket_name,
    Key=first_file_name
  )