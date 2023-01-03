import json
from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import markdown_text
from app.blocks.interactive.select_completed_tasks_blocks import select_completed_task_blocks
from app.db.db import Database


def out_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:

        slack_id = body["event"]["user"]
        channel_id: str = context['channel_id']
        is_dm = channel_id.startswith("D")

        if not is_dm:
            return

        db = Database()
        db.connect_to_database()

        participant = db.get_participant_by_slack_id(slack_id)[0]
        attendance = db.get_attendance_by_participant_id_where_out_time_null(participant['id'])
        in_progress_task = db.get_in_progress_task_by_participant_id(participant['id'])

        if not attendance or not in_progress_task:
            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=[markdown_text(markdown="You are not in")],
            )
            return

        tasks = list(map(lambda t: {
            "text": t["title"],
            "value": json.dumps(obj={
                "project_id": t['project_id'],
                "task_id": t['id'],
            })
        }, in_progress_task))

        client.chat_postMessage(
            channel=context['channel_id'],
            blocks=select_completed_task_blocks(tasks=tasks, payload='project name payload'),
        )

    except Exception as e:
        logger.error(e)
