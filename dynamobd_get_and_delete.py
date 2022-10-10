import boto3

table_name = 'employees' # provide / update table name here

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

response = table.get_item(
    Key={
        #'key': 'value'
        'emp_id': '2'
    }
)




