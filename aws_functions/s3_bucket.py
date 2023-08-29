def aws_s3_check_if_buckets_exists(s3):
    try:
        response = s3.list_buckets()
        buckets = []
        for bucket in response['Buckets']:
            buckets += {bucket['Name']}
    except Exception as e:
        print(f"the error occured during the executions is {e}")
        return False
    else:
        if buckets:
            return True
        else:
            return False
