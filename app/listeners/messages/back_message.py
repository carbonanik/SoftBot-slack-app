from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import markdown_text
from app.db.db import Database
from app.util.date_time import time_delta_to_str


def back_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
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
                blocks=[markdown_text(markdown="Start by sending start")]
            )
            return

        attendance = db.get_last_attendance_where_not_out(participant[0]['id'])

        if not attendance:
            client.chat_postMessage(
                channel=channel_id,
                blocks=[markdown_text(markdown="You are not in")]
            )
            return
        attendance_id = attendance[0]['id']
        print('==>', attendance_id)

        non_ended_break = db.get_not_ended_break(attendance_id)
        print(non_ended_break)

        if not non_ended_break:
            client.chat_postMessage(
                channel=channel_id,
                blocks=[markdown_text(markdown="You are not on break")]
            )
            return

        updated_break = db.update_ended_in_break(non_ended_break[0]['id'])
        started = updated_break[0]['started']
        ended = updated_break[0]['ended']

        time_difference = ended - started

        client.chat_postMessage(
            channel=channel_id,
            blocks=[markdown_text(markdown=f'You are back after {time_delta_to_str(time_difference)}')]
        )

    except Exception as e:
        logger.error(e)
