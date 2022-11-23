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

    # print(client)
    # print(message)
    # print(say)
    # print(context)

# ------------------------------------------ message response ----------------------------------------------------------
# {'ok': True,
# 'channel': 'C047Z9D3ADQ',
# 'ts': '1667719931.335599',
# 'message': {'bot_id': 'B040S4K565C',
# 'type': 'message',
# 'text': 'Hi!',
# 'user': 'U040J5JEFSB',
# 'ts': '1667719931.335599',
# 'app_id': 'A041B86RPKK',
# 'blocks':
# [{'type': 'header',
# 'block_id': 'X+Zm',
# 'text': {
# 'type': 'plain_text',
# 'text': 'This is a header block',
# 'emoji': True}}, {
# 'type': 'section',
# 'block_id': 'LcAL',
# 'text': {
# 'type': 'mrkdwn',
# 'text': 'This is a section block with a button.',
# 'verbatim': False},
# 'accessory': {
# 'type': 'button',
# 'action_id': 'test-button-click',
# 'text': {
# 'type': 'plain_text',
# 'text': 'Click Me',
# 'emoji': True},
# 'value': 'click_me_123'}}],
# 'team': 'T02NRMZN8NS',
# 'bot_profile': {
# 'id': 'B040S4K565C',
# 'app_id': 'A041B86RPKK',
# 'name': 'SoftBot',
# 'icons': {
# 'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png',
# 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png',
# 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'},
# 'deleted': False,
# 'updated': 1666036906,
# 'team_id': 'T02NRMZN8NS'
# }}}


# ------------------------------------------ message -------------------------------------------------------------------
# {'client_msg_id': 'f8d5b57e-ec23-4a3c-bd00-d0105d57652a',
# 'type': 'message',
# 'text': 'test',
# 'user': 'U02NVERT65B',
# 'ts': '1667714331.255979',
# 'blocks':
# [{'type': 'rich_text',
#   'block_id': 'lIgq',
#   'elements':
#   [{  'type':'rich_text_section',
#       'elements':
#       [{  'type': 'text',
#           'text': 'test'
#       }]
#   }]
# }],
# 'team': 'T02NRMZN8NS',
# 'channel':'C047Z9D3ADQ',
# 'event_ts': '1667714331.255979',
# 'channel_type': 'channel'
# }

# ------------------------------------------ context -------------------------------------------------------------------
# {'is_enterprise_install': False,
# 'team_id': 'T02NRMZN8NS',
# 'user_id': 'U02NVERT65B',
# 'channel_id': 'C047Z9D3ADQ',
# 'logger': <Logger bot.py (DEBUG)>,
# 'token': 'xoxb-2773747756774-4018188491895-bAdq7eMGa0nUkxNNtrBDbFXF',
# 'client': <slack_sdk.web.client.WebClient object at 0x7f8577afeb00>,
# 'authorize_result':
# {'enterprise_id': None,
# 'team_id': 'T02NRMZN8NS',
# 'bot_user_id': 'U040J5JEFSB',
# 'bot_id': 'B040S4K565C',
# 'bot_token': 'xoxb-2773747756774-4018188491895-bAdq7eMGa0nUkxNNtrBDbFXF',
# 'user_id': 'U02NVERT65B',
# 'user_token': None},
# 'bot_id': 'B040S4K565C',
# 'bot_user_id': 'U040J5JEFSB',
# 'bot_token': 'xoxb-2773747756774-4018188491895-bAdq7eMGa0nUkxNNtrBDbFXF',
# 'ack': <slack_bolt.context.ack.ack.Ack object at 0x7f8577afeb60>,
# 'say': <slack_bolt.context.say.say.Say object at 0x7f8577afea40>,
# 'respond': <slack_bolt.context.respond.respond.Respond object at 0x7f8577afec80>,
# 'matches': ('test',)
# }
