import json
from logging import Logger
from typing import List

from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.review_and_blockers_blocks import review_and_blockers_blocks
from app.db.db import Database


def select_completed_task_next_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        blocks = body['message']['blocks']

        all_visible_task = list(filter(lambda b: b['block_id'] == "task-to-mark", blocks))[0]['elements'][0]['options']
        selected_tasks: List = body['state']['values']['task-to-mark']['completed-task-select']['selected_options']

        unselected_tasks = [task for task in all_visible_task if task not in selected_tasks]

        blocker_project = None
        # print(list(map(lambda b: b['text']['text'], unselected_tasks)))

        db = Database()
        db.connect_to_database()

        if unselected_tasks:
            payload = unselected_tasks[0]['value']
            project_id = json.loads(s=payload)['project_id']
            blocker_project = db.get_project_by_id(str(project_id))[0]

            # task_payloads = list(map(lambda ut: ut['value'], unselected_tasks))

        review_task = list(map(lambda t: {"text": t['text']['text'], "value": json.loads(t['value'])}, selected_tasks))

        # print(review_task)
        projects_of_selected = list(set(map(lambda t: str(t['value']['project_id']), review_task)))
        # print()
        # return

        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=review_and_blockers_blocks(
                tasks=review_task,
                project=blocker_project,
                projects_ids=','.join(projects_of_selected)
            ),
            ts=body['container']['message_ts'],
        )
    except Exception as e:
        logger.error(e)
