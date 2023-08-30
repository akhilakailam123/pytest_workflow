

def aws_iam_check_if_policy_exist(iam, policy_arn_to_test):
    try:
        response = iam.get_policy(PolicyArn=policy_arn_to_test)
        return True
    except iam.exceptions.NoSuchEntityException:
        return False
    except Exception as e:
        print("error occurred while aws_iam_check_if_policy_exist, and error is {}".format(e))
        return False


def aws_iam_check_if_role_exist(iam, role_name_to_check):
    try:
        response = iam.get_role(RoleName=role_name_to_check)
        return True
    except iam.exceptions.NoSuchEntityException:
        return False
    except Exception as e:
        print("error occurred while aws_iam_check_if_role_exist, and error is {}".format(e))
        return False

