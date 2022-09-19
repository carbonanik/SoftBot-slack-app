import os
import logging

from slack_bolt import App
from app.listeners import register_listeners
from datetime import date
# import gspread

# Initialization
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SIGNING_SECRET")
)
logging.basicConfig(level=logging.DEBUG)

# gsc = gspread.service_account("service_account.json")
# sh = gsc.open("Attendance Sheet")
# wks = sh.worksheet("Current")

register_listeners(app)


if __name__ == '__main__':
    app.start(port=int(os.environ.get("PORT", 80)))

# def user_info(user_id: Str, client: WebClient):
#     try:
#         result = client.users_info(user=user_id)
#         # print(result)
#         return result
#     except SlackApiError as e:
#         logger.error("Error fetching conversations: {}".format(e))
