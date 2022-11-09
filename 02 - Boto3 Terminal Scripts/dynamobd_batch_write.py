# Batch write data to DynamoDB table

import boto3

# ---- UPDATE INPUTS HERE ---- #
table_name = 'employees-batch-demo'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

with table.batch_writer() as batch:
    for x in range(100): # loop through 100 entries as example
        batch.put_item(
            Item={
                'emp_id': str(x), # used as sample id value
                'name': f'Name-{x}' # used as sample name value
            }
        )

print('Batch writing complete.')
