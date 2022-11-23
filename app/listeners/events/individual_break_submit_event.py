from slack_bolt import Ack, BoltContext
from logging import Logger
from slack_sdk import WebClient
from app.blocks.response.you_are_on_break import you_are_on_break
from app.db.db import Database


def individual_break_submit_event(context: BoltContext, ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    print("fun fun ")
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]
    break_pac = state['individual_break_radio']['individual_break_select']['selected_option']['value']

    break_duration = {
        '1': "30 minutes",
        '2': "1 hour",
        '3': "2 hours"
    }

    print(break_pac)
    print("break_pac")

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

    # local_tz = user_info['tz']
    # us_eastern_tz = 'US/Eastern'

    db = Database()
    db.connect_to_database()

    res = db.insert_break_if_possible(slack_user_id, break_duration[break_pac])
    print(res)

    # last_in = db.get_last_in_for_user(slack_user_id)

    # in_datetime = last_in[0][4]
    # now_datetime = db.now_time()[0][0]
    # datetime.now(in_datetime)
    # print(now_datetime - in_datetime)
    if res:
        client.chat_postMessage(
            channel="#attendance-beta",
            blocks=you_are_on_break(name, break_duration[break_pac])
        )

    # data = wks.get_all_values()
    #
    # for i in range(len(data)):
    #     if data[i][loacl_date_col] == now_date_str(local_tz) and data[i][slack_id_col] == slack_user_id and data[i][
    #         out_local_time_col] == '':
    #
    #         prev_break_time_str = data[i][total_break_time_col]
    #         print(prev_break_time_str)
    #         prev_break_time = timedelta(minutes=0)
    #         print(prev_break_time)
    #
    #         if prev_break_time_str is not None and prev_break_time_str != '':
    #             prev_break_time = parse_time(prev_break_time_str)
    #             print('not none')
    #             print(prev_break_time)
    #
    #         break_time = prev_break_time + timedelta(minutes=m[break_pac])
    #         # print(break_time)
    #
    #         # wks.update(f'{col_letter[total_break_time_col]}{i+1}', time_delta_to_str(break_time), raw=False)
    #
    #         client.chat_postMessage(
    #             channel="#attendance-beta",
    #             blocks=you_are_on_break(name, f'{m[break_pac]} min')
    #         )
    #         break

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
