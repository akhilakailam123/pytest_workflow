import boto3
from aws_functions.s3_bucket import aws_s3_check_if_buckets_exists


def test_aws_s3_check_if_bucket_exists():
    s3 = boto3.client('s3')
    assert aws_s3_check_if_buckets_exists(s3) == True
