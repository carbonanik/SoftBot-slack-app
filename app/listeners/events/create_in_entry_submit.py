from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from service_account import wks
from app.util.date_time import now_date_str, now_time_str
from app.blocks.you_are_in_message import you_are_in
from app.util.const import loacl_date_col, us_date_col , col_letter,in_local_time_col,in_us_time_col, name_col, slack_id_col, working_on_col


def create_in_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]

    task_name = state["task_name"]["plain_text_input-action"]["value"]

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
    local_tz = user_info['tz']
    us_eastern_tz = 'US/Eastern'

    build_row = [None] * 20
    build_row.insert(name_col, name)
    build_row.insert(slack_id_col, slack_user_id)
    build_row.insert(working_on_col, task_name)

    wks.insert_row(build_row, index=2)
    wks.update(f'{col_letter[loacl_date_col]}2', now_date_str(local_tz), raw=False)
    wks.update(f'{col_letter[us_date_col]}2', now_date_str(us_eastern_tz), raw=False)
    wks.update(f'{col_letter[in_local_time_col]}2', now_time_str(local_tz), raw=False)
    wks.update(f'{col_letter[in_us_time_col]}2', now_time_str(us_eastern_tz), raw=False)

    client.chat_postMessage(
        channel="#soft-bot",
        blocks=you_are_in(
            name=name, 
            date=now_date_str(local_tz),
            task=task_name, 
            time=now_time_str(local_tz)
        )
    )

