from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import mrkdwn_text
from app.blocks.interactive.select_project import select_project
from app.db.db import Database


def in_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        slack_id = body["event"]["user"]
        channel_id: str = context['channel_id']
        is_dm = channel_id.startswith("D")

        if not is_dm:
            return

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        if not participant:
            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=[mrkdwn_text(markdown="To participate in attendance write `start`")]
            )
            return

        projects = db.get_projects()

        if not projects:
            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=[mrkdwn_text(markdown="No Project have been created")]
            )
            return

        project_arr_dict = list(map(lambda p: {"text": p["title"], "value": str(p["id"])}, projects))

        client.chat_postMessage(
            channel=context['channel_id'],
            blocks=select_project(projects=project_arr_dict)
        )

    except Exception as e:
        logger.error(e)
