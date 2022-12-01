from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient
from app.blocks.interactive.and_and_select_task_blocks import add_and_select_task_blocks
from app.db.db import Database


def select_project_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        project_id = body['state']['values']['projects-block']['select-project']['selected_option']['value']
        project_name = body['state']['values']['projects-block']['select-project']['selected_option']['text']['text']

        slack_id = context["user_id"]

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        uncompleted_task = db.get_task_uncompleted_filtered(
            participant[0]['id'],
            project_id
        )

        tasks = []
        for t in uncompleted_task:
            tasks.append({"text": t["title"], "value": str(t["id"])})

        select_task = add_and_select_task_blocks(
            project=project_name,
            tasks=tasks,
            hack_for_project_id=str(project_id)
        )

        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=select_task,
            ts=body['container']['message_ts'],
        )
    except Exception as e:
        logger.error(e)
