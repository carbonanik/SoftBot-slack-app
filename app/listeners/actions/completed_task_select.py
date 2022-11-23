from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient


def completed_task_select(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
