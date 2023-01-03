import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from app.features import register_features
from app.listeners import register_listeners

load_dotenv()
print(os.getenv("SLACK_BOT_TOKEN"))

app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SIGNING_SECRET")
)

logging.basicConfig(level=logging.ERROR)

register_listeners(app)
# register_features(app)

@app.message("joke")  # type: ignore
def show_random_joke(message, say):
    print("got message")
    """Send a random pyjoke back"""
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    # joke = pyjokes.get_joke()
    # logger.info(f"Sent joke < {joke} > to user {user_id}")

    say(text='joke', channel=dm_channel)


if __name__ == '__main__':
    handler = SocketModeHandler(app, os.getenv("SLACK_BOT_APP_LEVEL_TOKEN"))
    handler.start()
