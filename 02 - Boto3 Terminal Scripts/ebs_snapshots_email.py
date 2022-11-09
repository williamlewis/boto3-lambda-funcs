# Email list of EBS Snapshots based on tags

import boto3

ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

# define filter for EC2 instances tagged as 'Backup:  Yes'
backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]

# create list to store snapshot Ids
snapshot_ids = []

# loop through filtered LIST of EC2 instances in ec2.Instance collection
for instance in ec2.instances.filter(Filters=backup_filter): # call filter() method on instances collection of EC2 resource class 
    for vol in instance.volumes.all(): # loop through volumes of each filtered instance to create snapshot
        snapshot = vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)


# prepare str msg for SNS actions
sns_msg = 'Here is a list of EBS Volume Snapshots, gathered with Boto3 and sent via SNS' + '\n\n' + f'{snapshot_ids}'

# use publish() method on SNS class
sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:095304811476:snapshots', # provide Topic ARN from console
    Subject='EBS Snapshots',
    Message=sns_msg
)
