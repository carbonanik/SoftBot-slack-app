from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.block.block import markdown_text
from app.db.db import Database
from app.util.const import common_channel_id

break_times = {'1': '30 minutes', '2': '1 hour', '3': '2 hours', '4': '4 hours'}


def individual_break_select(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        selected = body['state']['values']['individual_break_radio']['individual_break_select']['selected_option']
        slack_id = context["user_id"]
        selected_time = break_times[selected['value']]

        user_info = client.users_info(user=slack_id)["user"]
        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

        db = Database()
        db.connect_to_database()

        participant = db.get_participant_by_slack_id(slack_id)
        attendance = db.get_last_attendance_where_not_out(participant[0]['id'])

        db.insert_break(selected_time, attendance[0]['id'])

        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=[markdown_text(markdown=f"You are on a {selected_time} break")],
            ts=body['container']['message_ts'],
        )

        client.chat_postMessage(
            channel=common_channel_id,
            blocks=[markdown_text(markdown=f"{name} on a {selected_time} break")],
        )

    except Exception as e:
        logger.error(e)
