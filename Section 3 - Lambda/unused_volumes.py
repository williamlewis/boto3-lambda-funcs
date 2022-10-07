import boto3
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

volumes = ec2_client.describe_volumes()
sns_arn = 'arn:aws:sns:us-east-1:095304811476:volume-alerts' # get actual SNS Topic ARN from console (placeholder used here)


# check for any unused EBS volumes (i.e. if they are not attached to any EC2 intance)
unused_volumes = []
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_volumes.append(volume['VolumeId'])



# compose email body to display Id of unused volumes
email_body = '##### Unused Volumes #####\n'

if len(unused_volumes) > 0:
    for vol in unused_volumes:
        email_body += f'VolumeId = {vol}'
else:
    email_body += 'No unused volumes were found.'



# send email summary of unused volumes using SNS
sns_client.publish(
    TopicArn=sns_arn,
    Message=email_body,
    Subject='Unused Volumes Summary'
)

