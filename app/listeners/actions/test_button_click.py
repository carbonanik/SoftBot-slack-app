from logging import Logger
from slack_bolt import BoltContext, Say, Ack
from slack_sdk import WebClient


def test_button_click(ack: Ack, body, client: WebClient, context: BoltContext, logger: Logger):
    ack()
    # print(ack)
    # print(body)
    # print(client)
    # print(context)
    # print(logger)
    print(body['container']['message_ts'])

    client.chat_update(
        channel=body['container']['channel_id'],
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
                    "text": "You Clicked the button."
                }
            }
        ],
        ts=body['container']['message_ts'],
    )


# -------------------------------------------- body ---------------------------------------
# {'type': 'block_actions',
# 'user': {'id': 'U02NVERT65B',
# 'username': 'shkhnk',
# 'name': 'shkhnk',
# 'team_id': 'T02NRMZN8NS'
# }, 'api_app_id': 'A041B86RPKK',
# 'token': 'WhZeL8jaksq091eEOcIbXt8Z',
# 'container': {
# 'type': 'message',
# 'message_ts': '1667717734.434459',
# 'channel_id': 'C047Z9D3ADQ',
# 'is_ephemeral': False},
# 'trigger_id': '4326148157013.2773747756774.d512909f4329140208f384cf0da0a7fe',
# 'team': {
# 'id': 'T02NRMZN8NS',
# 'domain': 'carbonanik'},
# 'enterprise': None,
# 'is_enterprise_install': False,
# 'channel': {
# 'id': 'C047Z9D3ADQ',
# 'name': 'attendance-beta'},
# 'message': {
# 'bot_id': 'B040S4K565C',
# 'type': 'message',
# 'text': 'Hi!',
# 'user': 'U040J5JEFSB',
# 'ts': '1667717734.434459',
# 'app_id': 'A041B86RPKK',
# 'blocks': [{
# 'type': 'header',
# 'block_id': 'az5Sq',
# 'text': {
# 'type': 'plain_text',
# 'text': 'This is a header block',
# 'emoji': True }}, {
# 'type': 'section',
# 'block_id': 'vae',
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
# 'team': 'T02NRMZN8NS'},
# 'state': {'values': {}},
# 'response_url': 'https://hooks.slack.com/actions/T02NRMZN8NS/4329095236210/VXoa1aqpjW8zwXSqnXLbXhhM',
# 'actions': [{
# 'action_id': 'test-button-click',
# 'block_id': 'vae',
# 'text': {
# 'type': 'plain_text',
# 'text': 'Click Me',
# 'emoji': True},
# 'value': 'click_me_123',
# 'type': 'button',
# 'action_ts': '1667717736.141536'}]}

# ----------------------------------------- context ---------------------------------------
# {'is_enterprise_install': False,
# 'team_id': 'T02NRMZN8NS',
# 'user_id': 'U02NVERT65B',
# 'channel_id': 'C047Z9D3ADQ',
# 'response_url': 'https://hooks.slack.com/actions/T02NRMZN8NS/4329095236210/VXoa1aqpjW8zwXSqnXLbXhhM',
# 'logger': <Logger bot.py (DEBUG)>,
# 'token': 'xoxb-2773747756774-4018188491895-bAdq7eMGa0nUkxNNtrBDbFXF',
# 'client': <slack_sdk.web.client.WebClient object at 0x7f74d2946350>,
# 'authorize_result': {
# 'enterprise_id': None,
# 'team_id': 'T02NRMZN8NS',
# 'bot_user_id': 'U040J5JEFSB',
# 'bot_id': 'B040S4K565C',
# 'bot_token': 'xoxb-2773747756774-4018188491895-bAdq7eMGa0nUkxNNtrBDbFXF',
# 'user_id': 'U02NVERT65B',
# 'user_token': None},
# 'bot_id': 'B040S4K565C',
# 'bot_user_id': 'U040J5JEFSB',
# 'bot_token': 'xoxb-2773747756774-4018188491895-bAdq7eMGa0nUkxNNtrBDbFXF',
# 'ack': <slack_bolt.context.ack.ack.Ack object at 0x7f74d2946410>,
# 'say': <slack_bolt.context.say.say.Say object at 0x7f74d29462f0>,
# 'respond': <slack_bolt.context.respond.respond.Respond object at 0x7f74d2946380>}
