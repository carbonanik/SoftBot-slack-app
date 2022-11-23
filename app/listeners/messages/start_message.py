from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import header, mrkdwn_text
from app.db.db import Database
from app.util.const import common_channel_id


def start_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        channel_id: str = context['channel_id']
        is_dm = channel_id.startswith("D")

        # print(channel_id)
        # print(is_dm)

        if not is_dm:
            return

        slack_id = body["event"]["user"]
        user_info = client.users_info(user=slack_id)["user"]
        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
        email = user_info['profile']['email']
        phone = user_info['profile']['phone']
        designation = user_info['profile']['title']

        db = Database()
        db.connect_to_database()
        inserted = db.insert_participant(slack_id, name, email, phone, designation)

        if inserted:
            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=[
                    mrkdwn_text(markdown="You have joined the attendance start by typing `in`")
                ],
                user=slack_id
            )
            client.chat_postMessage(
                channel=common_channel_id,
                blocks=[
                    mrkdwn_text(markdown="You have joined the attendance start by typing `in`")
                ],
                user=slack_id
            )
        else:
            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=[
                    mrkdwn_text(markdown="You are already participating in attendance, type `in`")
                ],
                user=slack_id
            )

        # print(user_info)

    except Exception as e:
        logger.error(e)
