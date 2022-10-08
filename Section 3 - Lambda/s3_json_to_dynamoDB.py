import boto3
import json


# PREPARATION:
# CREATE & ASSIGN ROLE FOR LAMBDA TO ACCESS S3 & DYNAMODB SERVICES (VIA CONSOLE)
# CREATE DYNAMODB TABLE FOR JSON DATA TO GO (VIA CONSOLE)

# #################################################
# ## CREATE S3 BUCKET WHERE JSON CAN BE UPLOADED ##
# #################################################
# s3_resource = boto3.resource('s3')
# bucket_name = 'demo-json-upload'
# s3_resource.create_bucket(
#     Bucket=bucket_name
# )
# print(f'Bucket "{bucket_name}" was successfully created.')


# #################################################
# ## CREATE LAMBDA FUNCTION TO PROCESS JSON DATA ##
# #################################################
s3_client = boto3.client('s3')
dynamodb_resource = boto3.resource('dynamodb')

# get bucket name & JSON filename (object key) from CloudWatch log event
bucket = event['Records'][0]['s3']['bucket']['name'] # response dict keys found in CloudWatch log event, created at file upload
json_filename = event['Records'][0]['s3']['object']['key']

# get object from bucket, get body from object, & deserialize body back into dict format like original
json_object = s3_client.get_object(Bucket=bucket,Key=json_filename)
json_file_reader = json_object['Body'].read() # call the read() method because value is a StreamingBody()
json_dict = json.loads(json_file_reader)

# get DynamoDB table & insert JSON file contents
table = dynamodb_client.Table('demo-employees')
table.put_item(Item=json_dict)


print(str(event))
return 'Hello from Lambda'


