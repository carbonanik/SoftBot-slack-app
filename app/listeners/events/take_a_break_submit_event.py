from datetime import timedelta
from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from service_account import wks

from app.util.date_time import now_date_str, now_time_str, parse_time, time_delta_to_str
from app.blocks.you_are_in_message import you_are_in
from app.blocks.you_are_on_break_message import you_are_on_break
from app.util.const import col_letter, total_break_time_col, loacl_date_col, slack_id_col, out_local_time_col


def take_a_break_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]
    break_pac = state['select_break']['options']['selected_option']['value']

    m = {
        '1': 5,
        '2': 10,
        '3': 20
    }

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

    local_tz = user_info['tz']
    us_eastern_tz = 'US/Eastern'

    data = wks.get_all_values()

    for i in range(len(data)):
        if data[i][loacl_date_col] == now_date_str(local_tz) and data[i][slack_id_col] == slack_user_id and data[i][out_local_time_col] == '':

            prev_break_time_str = data[i][total_break_time_col]
            print(prev_break_time_str)
            prev_break_time = timedelta(minutes=0)
            print(prev_break_time)

            if prev_break_time_str != None and prev_break_time_str != '':
                prev_break_time = parse_time(prev_break_time_str)
                print('not none')
                print(prev_break_time)

            break_time = prev_break_time + timedelta(minutes=m[break_pac])
            print(break_time)

            wks.update(f'{col_letter[total_break_time_col]}{i+1}', time_delta_to_str(break_time), raw=False)

            client.chat_postMessage(
                channel="#attendance-beta",
                blocks=you_are_on_break(name, f'{m[break_pac]} min')
            )
            break

    # sa = gspread.service_account()
    # sh = sa.open("Attendance Sheet")
    # wks = sh.worksheet("Current")

    # wks.insert_row([None, name, slack_user_id, task_name, None], index=2)
    # wks.update('A2', now_date_str(), raw=False)
    # wks.update('E2', now_time_str(), raw=False)

    # client.chat_postMessage(
    #     channel="#attendance-beta",
    #     blocks=you_are_in(
    #         name=name,
    #         date=now_date_str(),
    #         task=task_name,
    #         time=now_time_str()
    #     )
    # )
