from logging import Logger
from slack_bolt import BoltContext, Ack
from slack_sdk import WebClient
from app.blocks.block.block import header
from app.blocks.response.out_with_summery import out_with_summery
from app.db.db import Database
from app.util.const import common_channel_id
from app.util.date_time import time_delta_to_str, now_time_str


def review_blockers_submit(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    try:
        state = body['state']['values']
        slack_id = context["user_id"]

        print(state)

        user_info = client.users_info(user=slack_id)["user"]
        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
        local_tz = user_info['tz']

        db = Database()
        db.connect_to_database()
        participant = db.get_participant_by_slack_id(slack_id)[0]
        attendance = db.get_attendance_by_participant_id_where_out_time_null(participant['id'])[0]
        print(attendance)

        tasks_ids = []

        for s in state:
            if s.startswith('task-'):
                task_id = s.removeprefix('task-')
                tasks_ids.append(int(task_id))
                task_review = state[s]['plain_text_input-action']['value']

                db.task_update_ended_at(int(task_id))
                db.insert_review(task_review, int(task_id), participant['id'])

            elif s.startswith('project-'):
                project_id = s.removeprefix('project-')
                project_blocker = state[s]['plain_text_input-action']['value']

                db.insert_blocker(project_blocker, int(project_id), participant['id'])

        updated_attendance = db.update_attendance_out_time_by_id(attendance['id'])[0]
        worked_time = updated_attendance['out_time'] - updated_attendance['in_time']

        tasks = db.get_tasks_by_ids(tuple(tasks_ids))
        project = db.get_project_by_id(tasks[0]['project_id'])[0]

        blocks = out_with_summery(
            name=name,
            time=now_time_str(local_tz),
            hour=time_delta_to_str(worked_time),
            project=project['title'],
            tasks=list(map(lambda t: t['title'], tasks))
        )
        # [header(text=f"{name} out at {now_time_str(local_tz)}, worked {time_delta_to_str(worked_time)}")]

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

