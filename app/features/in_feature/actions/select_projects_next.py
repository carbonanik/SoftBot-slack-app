from logging import Logger

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.select_task_under_project_blocks_and_add_task import \
    select_task_under_project_and_add_task_blocks
from app.db.db import Database


def select_projects_next(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        # get selected data from state
        selected_projects = body['state']['values']['select-project']['project-selected']['selected_options']

        # do nothing if state empty
        if not selected_projects:
            return

        slack_id = context["user_id"]

        # init database
        db = Database()
        db.connect_to_database()

        participant = db.get_participant_by_slack_id(slack_id)

        project_task_dict = []

        for sp in selected_projects:
            tasks = db.get_task_uncompleted_filtered(
                participant[0]['id'],
                int(sp['value'])
            )
            project_task_dict.append(
                {
                    'project': sp['text']['text'].removesuffix('*').removeprefix('*'),
                    'tasks': list(map(lambda t: {'text': t['title'], 'value': str(t['id'])}, tasks)),
                    'value': sp['value']
                }
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
