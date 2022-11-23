from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient
from app.blocks.response.you_are_in import you_are_in
from app.db.db import Database
from app.util.const import common_channel_id
from app.util.date_time import now_time_str


def start_selected_task_action(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()

    try:
        slack_id = context["user_id"]
        user_info = client.users_info(user=slack_id)["user"]
        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
        local_tz = user_info['tz']

        try:
            selected_tasks = body['state']['values']['select-tasks']['task-selected']['selected_options']
        except:
            return

        tasks_ids = list(map(lambda t: t['value'], selected_tasks))
        tasks_titles = list(map(lambda t: t['text']['text'], selected_tasks))

        print(tasks_ids)

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)[0]
        attendance = db.insert_attendance(participant['id'])[0]

        print(participant)
        print(attendance)

        for tid in tasks_ids:
            db.task_update_started_at(tid)
            db.insert_relation_attendance_to_task(attendance['id'], int(tid))

        blocks = you_are_in(
            name=name,
            time=now_time_str(local_tz),
            tasks=tasks_titles
        )
        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=blocks,
            ts=body['container']['message_ts'],
        )
        client.chat_postMessage(
            channel=common_channel_id,
            blocks=blocks,
        )
    except Exception as e:
        logger.error(e)
