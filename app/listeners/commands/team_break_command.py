from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.blocks.modals.team_break_modal import team_break_modal
from app.blocks.modals.loading_modal import loading_modal
from app.blocks.modals.create_in_entry_modal import create_in_entry_modal
from app.blocks.time_modal import time_modal


def team_break_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        trigger_id = body["trigger_id"]
        loading_modal_response = client.views_open(
            trigger_id=trigger_id,
            view=loading_modal()
        )
        ack()

        client.views_update(
            view_id=loading_modal_response["view"]["id"],
            hash=loading_modal_response["view"]["hash"],
            view=team_break_modal()
        )

        # slack_user_id = body["user"]["id"]
        # print(body)

        # user_info = client.users_info(user=body['user_id'])
        # print(user_info['user']['tz'])

    except Exception as e:
        logger.error(e)
