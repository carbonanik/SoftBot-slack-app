from logging import Logger

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.block.block import markdown_text
from app.db.db import Database


def create_project(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        slack_id = context["user_id"]
        channel_id = body['container']['channel_id']

        try:
            project_name = body['state']['values']['project-name']['plain_text_input-action']['value']
        except:
            return

        try:
            project_description = body['state']['values']['project-description']['plain_text_input-action']['value']
        except:
            project_description = None

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        inserted = db.insert_project(
            project_name,
            project_description,
            int(participant[0]['id'])
        )

        if not inserted:
            client.chat_update(
                channel=channel_id,
                blocks=[markdown_text(markdown="Could not create the project")],
                ts=body['container']['message_ts'],
            )
            return

        client.chat_update(
            channel=channel_id,
            blocks=[markdown_text(markdown=f"Project {project_name} created")],
            ts=body['container']['message_ts'],
        )

    except Exception as e:
        logger.error(e)
