from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient
from slack_bolt import Respond
from curses import raw
# import gspread
from datetime import date

from app.blocks.modals.loading_modal import loading_modal


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


