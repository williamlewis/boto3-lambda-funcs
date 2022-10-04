import boto3
client = boto3.client('ec2')
resp = client.describe_instances()

# to get values from the Return dict, first loop through the Reservations item, then through the Instances items within that
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_type = instance['InstanceType']
        instance_id = instance['InstanceId']
        instance_az = instance['Placement']['AvailabilityZone']

        print(f'The {instance_type} instance with Id {instance_id} is hosted in the {instance_az} AZ.')
