from typing import List

from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.db.db import Database
# from service_account import wks

from app.blocks.response.daily_summery import daily_summery

from datetime import datetime, date, tzinfo
from pytz import timezone, all_timezones, utc


def daily_summery_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
    # try:
    ack()

    # slack_user_id = body['user_id']

    # user_info = client.users_info(user=slack_user_id)["user"]
    # todo open loading modals

    # list = client.users_list()['members']
    # for m in list:
    #     print(m)

    # name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
    # local_tz = user_info['tz']
    # us_eastern_tz = 'US/Eastern'

    db = Database()
    db.connect_to_database()
    participants: List = db.get_all_participant()
    today_in = db.get_last_attendance_of_day(date.today())

    present_list = []
    absent_list = []
    delayed_list = []

    bangladesh_timezone = 'Asia/Dhaka'

    tasks_list = []

    for i in today_in:
        tasks_list += i['tasks']

    for p in participants:
        print(p)
        for ti in today_in:
            if ti['slack_id'] == p['slack_id']:
                in_time = ti['in_time']

                # replacing the previous timezone with new one
                # it will not shift the time
                in_time = in_time.replace(tzinfo=utc)

                # shifting the time from previous to new one
                # this will shift time according to timezone
                in_time = in_time.astimezone(timezone(bangladesh_timezone))
                print(in_time.time())

                if in_time.time() > datetime.strptime('10:00', '%H:%M').time():
                    print("late")
                    delayed_list.append(ti['name'])
                else:
                    present_list.append(ti['name'])
            else:
                absent_list.append(p['name'])

    if not present_list:
        present_list.append('No one present')
    if not delayed_list:
        delayed_list.append('No one delayed')
    if not absent_list:
        delayed_list.append('No one absent')

    client.chat_postMessage(
        channel="#attendance-beta",
        blocks=daily_summery(
            date=date.today(),
            present_list=present_list,
            absent_list=absent_list,
            delayed_list=delayed_list,
            project_task=tasks_list
        )
    )

    # data = wks.get_all_values()
    #
    # for i in range(len(data)): if data[i][loacl_date_col] == now_date_str(local_tz) and data[i][slack_id_col]
    # == slack_user_id and data[i][out_local_time_col] == '':
    #
    #         wks.update(f'{col_letter[out_local_time_col]}{i+1}', now_time_str(local_tz), raw=False)
    #         wks.update(f'{col_letter[out_us_time_col]}{i+1}', now_time_str(us_eastern_tz), raw=False)
    #
    #         total_hour = calculate_total_hour(
    #             data[i][in_local_time_col],
    #             local_tz
    #         )
    #
    #         break_time_str = data[i][total_break_time_col]
    #         print(break_time_str)
    #         break_time = timedelta(minutes=0)
    #         print(break_time)
    #
    #         if break_time_str != None and break_time_str != '':
    #             break_time = parse_time(break_time_str)
    #             print('not none')
    #             print(break_time)
    #
    #         total_hour_minus_break = total_hour - break_time
    #
    #         total_str = time_delta_to_str(total_hour_minus_break)
    #
    #         wks.update(f'{col_letter[total_hour_col]}{i+1}', total_str, raw=False)

    # except Exception as e:
    #     logger.error(e)
