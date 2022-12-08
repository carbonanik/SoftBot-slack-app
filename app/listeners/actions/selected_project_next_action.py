from logging import Logger

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.select_task_under_project_blocks_and_add_task import \
    select_task_under_project_and_add_task_blocks
from app.db.db import Database


def select_project_next_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        selected_project = body['state']['values']['select-project']['project-selected']['selected_options']
        if not selected_project:
            return

        slack_id = context["user_id"]

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        project_task_dict = []

        for p in selected_project:
            project_name: str = p['text']['text'].removesuffix('*').removeprefix('*')
            project_id: int = int(p['value'])

            tasks = db.get_task_uncompleted_filtered(
                participant[0]['id'],
                project_id
            )
            tasks_dict = list(map(lambda t: {'text': t['title'], 'value': str(t['id'])}, tasks))

            project_task_dict.append(
                {'project': project_name, 'tasks': tasks_dict, 'value': str(project_id)}
            )

        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=select_task_under_project_and_add_task_blocks(
                project_task_dict=project_task_dict
            ),
            ts=body['container']['message_ts']
        )

    except Exception as e:
        logger.error(e)
