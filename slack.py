import json
import requests
import os

# Integração do Slack com nossa aplicação
def Slack(message):
    if os.path.exists('./config.json'):
        with open('config.json') as json_file:
            data = json.load(json_file)

            slackUrl: str = data['slack_url']

            if slackUrl != '':
                requests.post(slackUrl, data='{"text":"'+ message +'"}')
            else:
                print('You\'re not using Slack Integration')