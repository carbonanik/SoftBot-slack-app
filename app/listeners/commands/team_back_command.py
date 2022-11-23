from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.blocks.modals.individual_break_modal import individual_break_modal
from app.blocks.modals.loading_modal import loading_modal
from app.blocks.modals.create_in_entry_modal import create_in_entry_modal
from app.blocks.time_modal import time_modal
from app.db.db import Database
from app.blocks.response.team_is_back import team_is_back


def team_back_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()

        # slack_user_id = body['user_id']
        #
        # user_info = client.users_info(user=slack_user_id)["user"]
        #
        # name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
        # local_tz = user_info['tz']
        # us_eastern_tz = 'US/Eastern'

        db = Database()
        db.connect_to_database()
        # todo display team break ended information - when ended and how much time it took
        updated = db.update_team_break_ended()
        # print(updated)

        client.chat_postMessage(
            channel="#attendance-beta",
            blocks=team_is_back()
        )

        # client.views_update(
        #     view_id=loading_modal_response["view"]["id"],
        #     hash=loading_modal_response["view"]["hash"],
        #     view=individual_break_modal()
        # )

        # slack_user_id = body["user"]["id"]
        # print(body)

        # user_info = client.users_info(user=body['user_id'])
        # print(user_info['user']['tz'])

    except Exception as e:
        logger.error(e)
