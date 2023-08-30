def check_if_table_exists(dynamodb, table_name):
    try:
        response = dynamodb.list_tables()
        existing_tables = response['TableNames']

        if table_name in existing_tables:
            print(f"Table '{table_name}' exists.")
            return True
        else:
            print(f"Table '{table_name}' does not exist.")
            return False
    except Exception as e:
        print(f"An error occurred while checking if the table exists: {e}")
        return False
