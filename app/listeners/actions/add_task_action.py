from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient

from app.blocks.interactive.select_and_add_task import select_and_add_task
from app.db.db import Database


def add_task_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        slack_id = context["user_id"]

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)

        try:
            new_task_name = body['state']['values']['task-name']['plain_text_input-action']['value']
        except:
            return

        blocks = body['message']['blocks']
        block = list(filter(lambda b: b["block_id"] == "add-task", blocks))
        print(block)
        project_id = int(block[0]['elements'][0]['value'])

        inserted = db.insert_task(
            new_task_name,
            participant[0]['id'],
            project_id
        )

        project = db.get_project_by_id(project_id)

        uncompleted_task = db.get_task_uncompleted_filtered(
            participant[0]['id'],
            project_id
        )

        tasks = []
        for t in uncompleted_task:
            tasks.append({
                "text": t["title"],
                "value": str(t["id"])
            })

        if inserted:
            select_task = select_and_add_task(
                project=project[0]['title'],
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
