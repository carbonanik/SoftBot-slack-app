from logging import Logger

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.list_and_add_task_block import list_and_add_task_block
from app.db.db import Database


def select_project_when_add_task_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        project_id = body['state']['values']['projects-block'][
            'select-project-when-add-task'
        ]['selected_option']['value']

        project_name = body['state']['values']['projects-block'][
            'select-project-when-add-task'
        ]['selected_option']['text']['text']

        slack_id = context["user_id"]

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        all_tasks = db.get_tasks_project_id(project_id)

        tasks = list(map(lambda t: t["title"], all_tasks))

        print(tasks)

        select_task = list_and_add_task_block(
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
