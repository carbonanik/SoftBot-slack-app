from logging import Logger

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient


def in_message_project_selected_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
