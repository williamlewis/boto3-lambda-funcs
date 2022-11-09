from datetime import datetime, timedelta, timezone # import classes from datetime module

import boto3
ec2 = boto3.resource('ec2') # create an EC2 resource

snapshots = ec2.snapshots.filter(OwnerIds=['self']) # get only snapshots that I own (i.e. created)

for snapshot in snapshots:
    start_time = snapshot.start_time # get snapshot's start time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=15) # calculate threshold of 15 days ago
    if delete_time > start_time: # check if snapshot was created 15 days ago or more
        snapshot.delete() # delete old snapshot
        print(f'Snapshot with Id = {snapshot.snapshot_id} is deleted')
