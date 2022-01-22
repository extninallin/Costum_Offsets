from cgitb import text
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN_'])


def Send_Msg_to_channel(msj: str):
    client.chat_postMessage(channel='#melipediabot',
                            text=f":construction: {msj}")
# def Send_Msg_to_channel(msj: str):
#     client.chat_postMessage(channel='#melipediabot', blocks=[
#                             {"type": "section",
#                                  "text": {
#                                      "type": "mrkdwn",
#                                      "text": f"\n:construction:\n{msj}"}}])
