# Delete EBS snapshots older than 15 days

from datetime import datetime, timedelta, timezone # import classes from datetime module
import boto3

ec2 = boto3.resource('ec2')
snapshots = ec2.snapshots.filter(OwnerIds=['self']) # get only snapshots that I have created

for snapshot in snapshots:
    start_time = snapshot.start_time # get snapshot's start time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=15) # calculate threshold date of 15 days back from today

    if delete_time > start_time: # check if snapshot was created 15 days ago or more
        snapshot.delete() # delete old snapshot
        print(f'Snapshot with Id = {snapshot.snapshot_id} has been successfully deleted')
