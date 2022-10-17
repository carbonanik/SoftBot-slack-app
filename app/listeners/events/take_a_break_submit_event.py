from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from service_account import wks

# import gspread
from app.util.date_time import now_date_str, now_time_str
from app.blocks.you_are_in_message import you_are_in
from app.blocks.you_are_on_break_message import you_are_on_break


def take_a_break_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]
    break_pac = state['select_break']['options']['selected_option']['value']

    m = {
        '1': '5 min',
        '2': '10 min',
        '3': '20 min'
    }

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

    client.chat_postMessage(
        channel="#soft-bot",
        blocks=you_are_on_break(name, m[break_pac])
    )

    # sa = gspread.service_account()
    # sh = sa.open("Attendance Sheet")
    # wks = sh.worksheet("Current")

    # wks.insert_row([None, name, slack_user_id, task_name, None], index=2)
    # wks.update('A2', now_date_str(), raw=False)
    # wks.update('E2', now_time_str(), raw=False)

    # client.chat_postMessage(
    #     channel="#soft-bot",
    #     blocks=you_are_in(
    #         name=name,
    #         date=now_date_str(),
    #         task=task_name,
    #         time=now_time_str()
    #     )
    # )
