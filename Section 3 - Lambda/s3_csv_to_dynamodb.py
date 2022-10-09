import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
    
def csv_to_dynamodb(event, context):
    # get uploaded file from event response details
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    
    # read contents of CSV file & prepare data for DynamoDB
    csv_data = response['Body'].read() # call read() method because body is returned as a StreamingBody()
    csv_formatted = csv_data.decode('utf-8') # call decode() to convert from binary form to plain text
    employees = csv_formatted.split('\n')

    # persist data to DynamoDB (i.e. enter data in table)
    for emp in employees:
        emp_data = emp.split(',')
        try:
            table.put_item(
                Item={
                    'id': emp_data[0],
                    'name': emp_data[1],
                    'location': emp_data[2]
                    }
                )
        except Exception as e:
            print(f'Error:  not able to add item {emp} to DynamoDB')
