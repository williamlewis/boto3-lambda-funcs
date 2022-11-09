# Get and delete items from DynamoDB table

import boto3

# ---- UPDATE INPUTS HERE ---- #
table_name = 'employees'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# retrieve item(s) by key/value pair
response = table.get_item(
    Key={
        #'key': 'value'
        'emp_id': '2'
    }
)

# delete item(s) by key/value pair
table.delete_item(
    Key={
        #'key': 'value'
        'emp_id': '2'
    }
)
