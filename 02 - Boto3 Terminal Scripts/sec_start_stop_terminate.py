# Start, stop, & terminate instances based in Id

import boto3

client = boto3.client('ec2')

# start up an existing (previously stopped) EC2 instance using the InstanceId
client.start_instances(InstanceIds = ['i-0f2dfb8d2c411b5f8']) # argument is a *list* (**kwargs), so action can be perfored on multiple instances


# stop a running EC2 instance using the InstanceId
client.stop_instances(InstanceIds = ['i-0f2dfb8d2c411b5f8'])


# terminate an EC2 instance using the InstanceId
resp = client.terminate_instances(InstanceIds = ['i-0161a0beb43ff1127'])

for instance in resp['TerminatingInstances']:
    instance_id = instance['InstanceId']
    instance_cur_state = instance['CurrentState']['Name']

    print(f'The instance with Id {instance_id} has been Terminated')
    print(f'The instance\'s current state is {instance_cur_state}')
