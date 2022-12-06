from logging import Logger
from typing import List

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.response.daily_summery import daily_summery
from app.db.db import Database
from datetime import date, datetime
from pytz import utc, timezone

from app.util.const import common_channel_id


def summary_massage(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        channel_id: str = context['channel_id']
        is_dm = channel_id.startswith("D")

        if not is_dm:
            return

        db = Database()
        db.connect_to_database()

        participants: List = db.get_all_participant()
        attendances: List = db.get_last_attendance_of_day(date.today())
        attendance_ids = tuple(map(lambda a: a['id'], attendances))
        tasks = db.get_tasks_by_attendance_ids(attendance_ids)
        tasks_ids = tuple(map(lambda t: t['id'], tasks))
        projects = db.get_project_by_task_ids(tasks_ids)

        project_task = []

        for project in projects:
            tasks_of_project = list(filter(lambda t: t['project_id'] == project['id'], tasks))

            project_task.append({
                "project": project['title'],
                "tasks": list(map(lambda t: t['title'], tasks_of_project))
            })

        present_list = []
        absent_list = []
        delayed_list = []

        bangladesh_timezone = 'Asia/Dhaka'

        for participant in participants:
            attend = list(filter(lambda a: a['participant_id'] == participant['id'], attendances))

            if not attend:
                absent_list.append(participant['name'])
                continue

            in_time = attend[0]['in_time']

            in_time = in_time.replace(tzinfo=utc)
            in_time = in_time.astimezone(timezone(bangladesh_timezone))

            if in_time.time() > datetime.strptime('10:00', '%H:%M').time():
                delayed_list.append(participant['name'])
            else:
                present_list.append(participant['name'])

        if not present_list:
            present_list.append('No one present')
        if not delayed_list:
            delayed_list.append('No one delayed')
        if not absent_list:
            absent_list.append('No one absent')

        client.chat_postMessage(
            channel=context['channel_id'],
            blocks=daily_summery(
                date=date.today(),
                present_list=present_list,
                absent_list=absent_list,
                delayed_list=delayed_list,
                project_task=project_task
            )
        )

        client.chat_postMessage(
            text="open message to view summery",
            channel=common_channel_id,
            blocks=daily_summery(
                date=date.today(),
                present_list=present_list,
                absent_list=absent_list,
                delayed_list=delayed_list,
                project_task=project_task
            )
        )

    except Exception as e:
        logger.error(e)
