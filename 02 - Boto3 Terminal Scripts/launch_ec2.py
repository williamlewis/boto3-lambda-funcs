# Launch new intances based on AMI & instance type

import boto3

client = boto3.client('ec2')

resp = client.run_instances(
    # provide AMI id found in console; get from AMI Catalog or from instance launch dialog
    ImageId='ami-026b57f3c383c2eec',

    # define instance type, e.g. t2.micro for free tier
    InstanceType='t2.micro',
    
    # define min & max number of instances; e.g. set both to 1 to launch single instance
    MinCount=1,
    MaxCount=1
)

# from Return dict object, retrieve the InstanceID from Instances item
for instance in resp['Instances']:
    print(instance['InstanceId'])
