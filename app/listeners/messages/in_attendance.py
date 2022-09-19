from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient
from slack_bolt import Respond

def in_attendance(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        # print(context["respond"])
        greeting = context["matches"][0]
        print(body["event"]["text"])
        # say(f"{greeting}, how are you?")
    except Exception as e:
        logger.error(e)
