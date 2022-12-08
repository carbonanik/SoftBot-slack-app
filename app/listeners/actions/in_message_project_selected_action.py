from logging import Logger
from typing import List

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.review_and_blockers_blocks import review_and_blockers_blocks
from app.db.db import Database


def in_message_project_selected_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
