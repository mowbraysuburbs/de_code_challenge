import boto3
import config

s3_client = boto3.client(
    's3',
    region_name='af-south-1',
    aws_access_key_id=config.S3_ACCESS_KEY,
    aws_secret_access_key=config.S3_SECRET_KEY
)

BUCKET = 'cct-ds-code-challenge-input-data'
REGION = 'af-south-1'
