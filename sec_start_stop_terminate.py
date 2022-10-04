from pydoc import cli
import boto3
client = boto3.client('ec2')

# can start up a previously stopped EC2 instance using the InstanceId
# argument is a *list* (**kwargs), so action can be perfored on multiple instances by including multiple Ids in list
client.start_instances(InstanceIds = ['i-0f2dfb8d2c411b5f8'])

# stop a running EC2 instance using the InstanceId
client.stop_instances(InstanceIds = ['i-0f2dfb8d2c411b5f8'])

# terminate an EC2 instance using the InstanceId
client.terminate_instances(InstanceIds = ['i-0f2dfb8d2c411b5f8'])