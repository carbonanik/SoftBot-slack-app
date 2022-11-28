from logging import Logger
from slack_bolt import BoltContext, Say
from slack_sdk import WebClient


def test_message(client: WebClient, message, say: Say, context: BoltContext, logger: Logger):
    m = client.chat_postMessage(
        channel=context['channel_id'],
        text="Hi!",
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "This is a header block",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a section block with a button."
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "test-button-click"
                }
            }
        ]
    )

    print(m)

#---------------------------------------
