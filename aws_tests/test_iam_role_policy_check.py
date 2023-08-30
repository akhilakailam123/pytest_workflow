import boto3

from aws_functions.iam_role_policy_check import aws_iam_check_if_policy_exist, aws_iam_check_if_role_exist

# Create IAM client
iam = boto3.client('iam')

def test_aws_iam_check_if_policy_exist():
    policy_arn_to_check = 'arn:aws:iam::997609234031:policy/dynamodb_crudOperations'
    assert aws_iam_check_if_policy_exist(iam, policy_arn_to_check) is True

def test_aws_iam_check_if_role_exist():
    role_name_to_check = 'apigateway-lambda-role-6xuomjhw'
    assert aws_iam_check_if_role_exist(iam, role_name_to_check) is True
