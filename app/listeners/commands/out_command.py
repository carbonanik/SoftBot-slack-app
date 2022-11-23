from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.db.db import Database
# from service_account import wks
# from datetime import timedelta

from app.blocks.response.you_are_out import you_are_out
from app.util.date_time import now_date_str, now_time_str, calculate_total_hour, parse_time, time_delta_to_str, time_delta_to_str


def out_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()

        slack_user_id = body['user_id']

        user_info = client.users_info(user=slack_user_id)["user"]

        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
        # local_tz = user_info['tz']
        # us_eastern_tz = 'US/Eastern'

        db = Database()
        db.connect_to_database()
        # todo access updated attendance in dict manner
        updated_attendance = db.update_out_time(slack_user_id)
        print(updated_attendance)

        client.chat_postMessage(
            channel="#attendance-beta",
            blocks=you_are_out(
                name=name,
                duration=time_delta_to_str(updated_attendance[0][6]),
                tasks=updated_attendance[0][3]
            )
        )

        # data = wks.get_all_values()
        #
        # for i in range(len(data)):
        #     if data[i][loacl_date_col] == now_date_str(local_tz) and data[i][slack_id_col] == slack_user_id and data[i][out_local_time_col] == '':
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
        #
        #         client.chat_postMessage(
        #             channel="#attendance-beta",
        #             blocks=you_are_out(
        #                 name=data[i][name_col],
        #                 date=now_date_str(local_tz),
        #                 task=data[i][working_on_col],
        #                 time=now_time_str(local_tz),
        #                 working=total_hour,
        #             )
        #         )

    except Exception as e:
        logger.error(e)
