import os
import logging

from slack_bolt import App
from app.listeners import register_listeners
from datetime import date
from dotenv import load_dotenv

# Initialization
load_dotenv()
print(os.getenv("PORT"))

# print('secret here ---------------------')
# print(os.getenv("SLACK_BOT_TOKEN"))
# print(os.getenv("SIGNING_SECRET"))

app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SIGNING_SECRET")
)
logging.basicConfig(level=logging.DEBUG)

register_listeners(app)


if __name__ == '__main__':
    app.start(port=int(os.getenv("PORT", 5050)))

# def user_info(user_id: Str, client: WebClient):
#     try:
#         result = client.users_info(user=user_id)
#         # print(result)
#         return result
#     except SlackApiError as e:
#         logger.error("Error fetching conversations: {}".format(e))
