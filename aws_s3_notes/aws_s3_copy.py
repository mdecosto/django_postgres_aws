import boto3

s3_resource = boto3.resource('s3')

first_bucket_name = 'firstpythonbucket905cddd4-c102-4b8e-a561-2a313bcc689b'
first_file_name = '65c792firstfile.txt'
second_bucket_name = 'secondpythonbucketaeab37f2-2198-49e2-ae3d-363fb2343d0f'

def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)
copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)