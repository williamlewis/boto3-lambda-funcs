import boto3
client = boto3.client('s3')

# ---- UPDATE INPUTS HERE ---- #
bucket_name = ''
object_key = ''
sql_query = 'Select s.name, s.email from S3Object'

response = client.select_object_content(
    Bucket=bucket_name,
    Key=object_key,
    Expression=sql_query,
    ExpressionType='SQL',
    InputSerialization={'CSV':{'FileHeaderInfo':'Use'}},
    OutputSerialization={'CSV':{}}
)

# loop through payload object
for event in response['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode())
