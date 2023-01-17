import boto3

s3_resource = boto3.resource('s3')

first_bucket_name = '123pythonbucketeecc64d8-a1e4-403d-b7a6-7937dc86e95e'
first_file_name = '1115ca123file.txt'

s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'{first_file_name}') # Python 3.6+

# will be saved in tmp folder