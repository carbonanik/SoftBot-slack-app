from slack_bolt import Ack, BoltContext
from logging import Logger
from slack_sdk import WebClient

from app.blocks.modals.loading_modal import loading_modal
from app.blocks.modals.create_in_entry_modal import create_in_entry_modal


def in_command(context: BoltContext, ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        print(context.get('db'))
        trigger_id = body["trigger_id"]
        loading_modal_response = client.views_open(
            trigger_id=trigger_id,
            view=loading_modal()
        )
        ack()

        # print(loading_modal_response['view']['id'])
        client.views_update(
            view_id=loading_modal_response['view']['id'],
            hash=loading_modal_response["view"]["hash"],
            view=create_in_entry_modal()
        )

        # task 1,
        # task 2,
        # task 3

    except Exception as e:
        logger.error(e)
