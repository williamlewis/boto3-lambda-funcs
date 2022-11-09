# Use EC2 resource collections to filter & manage instances

import boto3

ec2 = boto3.resource('ec2') # define as a RESOURCE object, not a CLIENT object

# without filtering, loop through all instances and print their attributes
for instance in ec2.instances.all():
    print(f'Instance Id is {instance.instance_id} and instance type is {instance.instance_type}')


# get instance attributes filtered down to a specific AZ
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1b'] # define AZ here
    }
]):
    print(f'Instance Id is {instance.instance_id} and instance type is {instance.instance_type}')


# get instances in a running state, then stop them using the .stop() method (no loop needed)
ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]).stop()
