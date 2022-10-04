from itertools import count
import boto3
client = boto3.client('ec2')

client.run_instances(
    # provide AMI id found in console; get from AMI Catalog or from instance launch dialog
    ImageId='ami-026b57f3c383c2eec',

    # define instance type, e.g. t2.micro for free tier
    InstanceType='a1.medium'|'a1.large'|'a1.xlarge',
    
    # define min & max number of instances; both set at 1 for demo
    MinCount=1,
    MaxCount=1
)
