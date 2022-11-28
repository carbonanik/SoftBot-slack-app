from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import mrkdwn_text
from app.blocks.interactive.select_individual_break import select_individual_break
from app.db.db import Database


def break_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
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
                channel=channel_id,
                blocks=[mrkdwn_text(markdown="Start by sending start")]
            )
            return

        attendance = db.get_last_attendance_where_not_out(participant[0]['id'])

        if not attendance:
            client.chat_postMessage(
                channel=channel_id,
                blocks=[mrkdwn_text(markdown="You are not in")]
            )
            return
        print('==>', attendance[0]['id'])

        non_ended_break = db.get_not_ended_break(attendance[0]['id'])
        print(non_ended_break)

        if non_ended_break:
            client.chat_postMessage(
                channel=channel_id,
                blocks=[mrkdwn_text(markdown="You are already on a break")]
            )
            return

        client.chat_postMessage(
            channel=channel_id,
            blocks=select_individual_break()
        )

    except Exception as e:
        logger.error(e)
