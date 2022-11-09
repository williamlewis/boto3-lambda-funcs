# Check for unattached (unused) EBS volumes and send alert email using SNS

import boto3

ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

volumes = ec2_client.describe_volumes()
sns_arn = 'arn:aws:sns:us-east-1:095304811476:volume-alerts' # get SNS Topic ARN from console


def email_unused_volumes(event, context):
    
    # check for any unused EBS volumes (i.e. those not attached to any EC2 instance)
    unused_volumes = []
    total_unused_vol_size = 0
    for volume in volumes['Volumes']:
        if len(volume['Attachments']) == 0:
            unused_volumes.append(volume['VolumeId'])
            total_unused_vol_size += volume['Size']

    # compose email body to display Id of unused volumes & summarize total size not in use
    email_body = '##### Unused Volumes #####\n'
    if len(unused_volumes) > 0:
        for vol in unused_volumes:
            email_body += f'VolumeId = {vol}'
    else:
        email_body += 'No unused volumes were found.'
    email_body += f'\n\nThe total size of currently unused volumes is {total_unused_vol_size} GB.' # include a footnote summarizing storage size of all unused volumes

    # send email summary of unused volumes using SNS
    sns_client.publish(
        TopicArn=sns_arn,
        Message=email_body,
        Subject='Unused Volumes Summary'
    )

    return None
