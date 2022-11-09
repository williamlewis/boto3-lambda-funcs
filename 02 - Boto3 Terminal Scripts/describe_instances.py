# Describe instances and related attributes

import boto3

client = boto3.client('ec2')


# get values from the Return dict by looping through the Reservations item, then through the Instances items within that
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_type = instance['InstanceType']
        instance_id = instance['InstanceId']
        instance_az = instance['Placement']['AvailabilityZone']

        print(f'The {instance_type} instance with Id {instance_id} is hosted in the {instance_az} AZ.')


# get description of a *subset* of EC2 instances by using optional Filters argument of the describe_instances() method
resp = client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']
    }])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        print(f'Instance Id is {instance_id}')


# get description of EC2 instances with a certain tag only
resp = client.describe_instances(Filters=[{
    'Name': 'tag:Env',
    'Values': ['Dev']
    }])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        print(f'Instance Id is {instance_id}')
