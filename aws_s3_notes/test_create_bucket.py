import boto3

aws_access_key_id_value='AKIA5OGZGBM6XDSPP3HD'
aws_secret_access_key_value='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'
Bucket_value='test_create_delete'
LocationConstraint_value='REGION-FOR-S3-BUCKET'


client = boto3.resource(
    service_name='s3',
    aws_access_key_id=aws_access_key_id_value,
    aws_secret_access_key=aws_secret_access_key_value
)
client.create_bucket(Bucket=Bucket_value, CreateBucketConfiguration={'LocationConstraint': LocationConstraint_value})



# def resource(
#     self,
#     service_name,
#     region_name=None,
#     api_version=None,
#     use_ssl=True,
#     verify=None,
#     endpoint_url=None,
#     aws_access_key_id=None,
#     aws_secret_access_key=None,
#     aws_session_token=None,
#     config=None,
# ):
#   pass