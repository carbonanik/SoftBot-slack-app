from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient
from app.blocks.response.you_are_in import you_are_in
from app.db.db import Database
from app.util.const import common_channel_id
from app.util.date_time import now_time_str


def start_selected_tasks_in_multiple_project_action(ack: Ack, body, client: WebClient, context: BoltContext,
                                                    logger: Logger):
    ack()

    try:
        slack_id = context["user_id"]
        user_info = client.users_info(user=slack_id)["user"]
        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
        local_tz = user_info['tz']

        projects_payload = body['actions'][0]['value']

        statest = body['state']['values']

        selected_tasks = []
        for key in statest:
            if key.startswith('task-under-project-'):
                selected_tasks += statest[key]['task-under-project-selected']['selected_options']

        if not selected_tasks:
            return

        tasks_ids = list(map(lambda t: t['value'], selected_tasks))
        tasks_titles = list(map(lambda t: t['text']['text'], selected_tasks))

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)[0]
        attendance = db.insert_attendance(participant['id'])[0]

        for tid in tasks_ids:
            db.task_update_started_at(tid)
            db.insert_relation_attendance_to_task(attendance['id'], int(tid))

        tasks = db.get_tasks_by_ids(tuple(tasks_ids))

        project = db.get_project_by_id(tasks[0]['project_id'])[0]

        blocks = you_are_in(
            name=name,
            time=now_time_str(local_tz),
            project=projects_payload,
            tasks=tasks_titles
        )
        client.chat_update(
            channel=body['container']['channel_id'],
            blocks=blocks,
            ts=body['container']['message_ts'],
        )
        client.chat_postMessage(
            text=f'{name} In at {now_time_str(local_tz)}',
            channel=common_channel_id,
            blocks=blocks,
        )
    except Exception as e:
        logger.error(e)
