import boto3

s3_resource = boto3.resource('s3')

first_bucket_name = 'firstpythonbucket905cddd4-c102-4b8e-a561-2a313bcc689b'
first_file_name = '65c792firstfile.txt'

s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'{first_file_name}') # Python 3.6+

# will be saved in tmp folder