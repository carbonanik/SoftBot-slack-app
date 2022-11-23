from logging import Logger
from typing import List

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.review_and_blockers import review_and_blockers
from app.db.db import Database


def select_completed_task_next_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        blocks = body['message']['blocks']
        print(blocks)

        all_visible_task = list(filter(lambda b: b['block_id'] == "task-to-mark", blocks))[0]['elements'][0]['options']
        selected_tasks: List = body['state']['values']['task-to-mark']['completed-task-select']['selected_options']
        unselected_tasks = [task for task in all_visible_task if task not in selected_tasks]

        project = None
        if unselected_tasks:
            project_id = blocks[1]['elements'][1]['value']
            print(project_id)

            db = Database()
            db.connect_to_database()
            project = db.get_project_by_id(str(project_id))[0]

        review_task = list(map(lambda t: {"text": t['text']['text'], "value": t['value']}, selected_tasks))

        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=review_and_blockers(
                tasks=review_task,
                project=project
            ),
            ts=body['container']['message_ts'],
        )
    except Exception as e:
        logger.error(e)
