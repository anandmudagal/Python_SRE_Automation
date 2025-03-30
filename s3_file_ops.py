# s3_file_ops.py
import boto3
import logging

logger = logging.getLogger(__name__)

def list_s3_files(bucket_name, prefix=''):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    files = [obj['Key'] for obj in response.get('Contents', [])]
    logger.info(f"S3 Files in {bucket_name}/{prefix}: {files}")
    return files

def download_file(bucket_name, key, dest_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, key, dest_path)
    result = f"Downloaded {key} to {dest_path}"
    logger.info(result)
    return result
