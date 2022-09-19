from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient
from slack_bolt import Respond
from curses import raw
# import gspread
from datetime import date

from app.blocks.loading_modal import loading_modal

def in_attendance_to_google_spread_sheet(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        # print(context["respond"])
        user_id = body["event"]["user"]
        print(body["event"]["blocks"][0]["block_id"])

        # client.views_update(
        #     view_id=body["event"]["blocks"][0]["block_id"],
        #     view=loading_modal()
        # )

        user_info = client.users_info(user=user_id)["user"]

        name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

        # today_date = _today()

        # sa = gspread.service_account()
        # sh = sa.open("Attendance Sheet")
        # wks = sh.worksheet("Current")

        # wks.insert_row([today_date, name, user_id], index=2)

        say(f"{name}, You are in.")

    except Exception as e:
        logger.error(e)


def _today():
    d = date.today()
    full_date = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
    return full_date



# {'token': 'WhZeL8jaksq091eEOcIbXt8Z', 
# 'team_id': 'T02NRMZN8NS', 'api_app_id': 'A041B86RPKK', 'event': 
# {'client_msg_id': '9b75d79c-db04-4ba2-8629-ab9d8f2202a2', 'type': 'message', 'text': 'in', 'user': 'U02NVERT65B', 'ts': '1662902012.610759', 'team': 'T02NRMZN8NS', 'blocks': 
# [{'type': 'rich_text', 'block_id': 'FEQE4', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'in'}]}]}], 'channel': 'C040J7YHWET', 'event_ts': '1662902012.610759', 'channel_type': 'channel'}, 'type': 'event_callback', 'event_id': 'Ev041TQDE7A9', 'event_time': 1662902012, 'authorizations': [{'enterprise_id': None, 'team_id': 'T02NRMZN8NS', 'user_id': 'U040J5JEFSB', 'is_bot': True, 'is_enterprise_install': False}], 'is_ext_shared_channel': False, 'event_context': '4-eyJldCI6Im1lc3NhZ2UiLCJ0aWQiOiJUMDJOUk1aTjhOUyIsImFpZCI6IkEwNDFCODZSUEtLIiwiY2lkIjoiQzA0MEo3WUhXRVQifQ'}