from app.blocks.block.block import mrkdwn_text


def send_direct_message(client, channel_id):
    client.chat_postMessage(
        channel=channel_id,
        blocks=[mrkdwn_text(markdown="Send direct message to the bot")]
    )
