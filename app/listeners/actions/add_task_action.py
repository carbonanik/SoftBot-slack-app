from logging import Logger

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.select_task_under_project_blocks_and_add_task import \
    select_task_under_project_and_add_task_blocks
from app.db.db import Database


def add_task_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        blocks = body['message']['blocks']

        projects_id = []
        for b in blocks:
            bid: str = b['block_id']
            if bid.startswith('add-task-'):
                projects_id = b['elements'][0]['value'].split(",")
                break

        add_task_project_id = body['actions'][0]['block_id'].removeprefix('add-task-')
        add_task_project_id = int(add_task_project_id)

        try:
            task_to_add = body['state']['values'][
                f'task-name-{add_task_project_id}']['plain_text_input-action']['value']
        except:
            return

        print(task_to_add)

        slack_id = context['user_id']

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        inserted = db.insert_task(
            task_to_add,
            participant[0]['id'],
            add_task_project_id
        )

        if not inserted:
            return

        projects = db.get_projects_by_ids(tuple(map(lambda pid: int(pid), projects_id)))

        project_task_dict = []

        for p in projects:
            project_name: str = p['title']
            project_id: int = p['id']

            tasks = db.get_task_uncompleted_filtered(
                participant[0]['id'],
                project_id
            )
            tasks_dict = list(map(lambda t: {'text': t['title'], 'value': str(t['id'])}, tasks))

            project_task_dict.append(
                {'project': project_name, 'tasks': tasks_dict, 'value': str(project_id)}
            )

        select_task = select_task_under_project_and_add_task_blocks(
            project_task_dict=project_task_dict
        )

        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=select_task,
            ts=body['container']['message_ts'],
            metadata={}
        )

    except Exception as e:
        logger.error(e)
