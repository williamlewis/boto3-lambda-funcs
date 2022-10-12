import boto3
import os # use env variables to avoid hard coding the email addresses for sender & recipient 

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

# set email addresses as environmental variables of Lambda function via console (match Keys to variable names below)
# Note:  email addresses must be verified after being saved in SES via console
FROM_MAIL = os.environ['FROM_MAIL']
TO_MAIL = os.environ['TO_MAIL']


def find_unused_eips(event, context):
    
    ec2_resp = ec2_client.describe_addresses()
    unused_eips = []
    for address in ec2_resp['Addresses']:
        if 'InstanceId' not in address: # lack of InstanceId key in return dict means the EIP is unused (because no instance is utilizing it)
            unused_eips.append(address['PublicIp'])
    
    
    email_subject = 'Alert:  Unused Elastic IPs'
    email_body = 'Currently Unused Elastic IPs:\n'
    for eip in unused_eips:
        email_body += eip, '\n'
    

    ses_resp = ses_client.send_email(
        Source=FROM_MAIL,
        Destination={
            'ToAddresses': [
                TO_MAIL,
            ]
        },
        Message={
            'Subject': {
                'Data': email_subject,
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': email_body,
                    'Charset': 'utf-8'
                }
            }
        }
    )

    return None