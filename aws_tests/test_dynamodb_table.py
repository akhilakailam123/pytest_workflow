import boto3
from aws_functions.dynamodb_table import check_if_table_exists


def test_check_if_table_exists():
    dynamodb = boto3.client('dynamodb')
    table_name = 'dynamo-table'
    assert check_if_table_exists(dynamodb,table_name) is True
