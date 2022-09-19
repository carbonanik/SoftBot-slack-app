from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from service_account import wks

# import gspread
from app.util.date_time import now_date_str, now_time_str
from app.blocks.you_are_in_message import you_are_in


def create_in_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]

    task_name = state["task_name"]["plain_text_input-action"]["value"]

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]


    # sa = gspread.service_account()
    # sh = sa.open("Attendance Sheet")
    # wks = sh.worksheet("Current")

    wks.insert_row([None, name, slack_user_id, task_name, None], index=2)
    wks.update('A2', now_date_str(), raw=False)
    wks.update('E2', now_time_str(), raw=False)

    client.chat_postMessage(
        channel="#soft-bot",
        blocks=you_are_in(
            name=name, 
            date=now_date_str(),
            task=task_name, 
            time=now_time_str()
        )
    )

