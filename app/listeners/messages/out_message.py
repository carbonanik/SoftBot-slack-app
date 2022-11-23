from logging import Logger
from slack_bolt import BoltContext, Say
from slack_sdk import WebClient
from app.blocks.block.block import mrkdwn_text
from app.blocks.interactive.select_completed_tasks import select_completed_task
from app.blocks.interactive.select_project import select_project
from app.db.db import Database


def out_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:

        slack_id = body["event"]["user"]
        channel_id: str = context['channel_id']
        is_dm = channel_id.startswith("D")

        # print(channel_id)
        # print(is_dm)

        if not is_dm:
            return

        db = Database()
        db.connect_to_database()

        participant = db.get_participant_by_slack_id(slack_id)[0]
        attendance = db.get_attendance_by_participant_id_where_out_time_null(participant['id'])
        in_progress = db.get_in_progress_task_by_participant_id(participant['id'])

        if in_progress and attendance:
            tasks = []
            for t in in_progress:
                tasks.append({"text": t["title"], "value": str(t["id"])})

            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=select_completed_task(tasks=tasks, hack_for_project_id=str(in_progress[0]["project_id"])),
            )
        else:
            client.chat_postMessage(
                channel=context['channel_id'],
                blocks=[mrkdwn_text(markdown="You are not in")],
            )

    except Exception as e:
        logger.error(e)
