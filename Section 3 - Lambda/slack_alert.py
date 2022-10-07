import requests
import json
import os

slack_web_hook = os.environ['SLACK_WEBHOOK'] # pass in slack web hook URL as an environmental variable, using the os module & setting the env var in the console
# in real use cases, be sure to encrypt the environmental variable (e.g. with KMS) and update code with related ENCRYPTED and DECRYPTED variables

def send_slack(event, context):
    print(str(event))
    slack_msg = {'text': 'EC2 Instance Stopped'}
    response = requests.post(slack_web_hook, data=json.dumps(slack_msg)) # use json.dumps() to convert slack_msg dictionary to text
    return response.text
