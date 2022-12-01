from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import markdown_text, header, multiline_text_input
from app.blocks.interactive.and_and_select_task_blocks import plain_text_input, actions, button_element
from app.db.db import Database


def add_project_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
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

        client.chat_postMessage(
            channel=channel_id,
            blocks=[
                header(text='Add new project 📙'),
                plain_text_input(
                    action_id="plain_text_input-action",
                    text="Project Name ",
                    block_id="project-name"
                ),
                multiline_text_input(
                    label='Description ',
                    block_id='project-description',
                    action_id='plain_text_input-action',
                    placeholder='Write a short description of the project',
                ),
                actions(elements=[
                    button_element(text="Create", value='0', action_id="create-project", style="danger")
                ], block_id="create-project"),
            ]
        )
    except Exception as e:
        logger.error(e)
