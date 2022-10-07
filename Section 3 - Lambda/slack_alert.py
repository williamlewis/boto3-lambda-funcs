from urllib import response
import requests
import json

slack_web_hook = '' # enter hooks.slack.com/services/... URL here (HTTPS)

def send_slack(event, context):
    print(str(event))
    slack_msg = {'text': 'EC2 Instance Stopped'}
    response = requests.post(slack_web_hook, data=json.dumps(slack_msg)) # use json.dumps() to convert slack_msg dictionary to text
    return response.text
