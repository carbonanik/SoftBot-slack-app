from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.blocks.loading_modal import loading_modal
from app.blocks.create_in_entry_modal import create_in_entry_modal
from app.blocks.take_a_break_radio_select_modal import take_a_break_radio_select_modal
from app.blocks.time_modal import time_modal

def break_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
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
            view=take_a_break_radio_select_modal()
        )

    except Exception as e:
        logger.error(e)