from typing import List


def header(text):
    return {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": text,
            "emoji": True
        }
    }


def divider():
    return {
        "type": "divider"
    }


def mrkdwn_text(markdown):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": markdown
        }
    }


def context_text(text):
    return {
        "type": "context",
        "elements": [
            {
                "type": "plain_text",
                "text": text,
                "emoji": True
            }
        ]
    }


def multiline_text_input(label, placeholder, block_id, action_id):
    return {
        "type": "input",
        "block_id": block_id,
        "element": {
            "type": "plain_text_input",
            "action_id": action_id,
            "multiline": True,
            "placeholder": {
                "type": "plain_text",
                "text": placeholder
            }
        },
        "label": {
            "type": "plain_text",
            "text": label,
            "emoji": True
        }
    }


def radio_button_select(label, block_id, action_id, options):
    return {
        "type": "input",
        "block_id": block_id,
        "label": {
            "type": "plain_text",
            "text": label,
            "emoji": True
        },
        "element": {
            "type": "radio_buttons",
            "action_id": action_id,
            "options": [text_option(text=option["text"], value=option["value"]) for option in options]
        }
    }


def text_option(text, value):
    return {
        "text": {
            "type": "mrkdwn",
            "text": text,
        },
        "value": value
    }


def titled_list(title, emoji, items: List):
    return f'*{title}*\n\n' + ''.join([f'{emoji} {item} \n' for item in items]) + '\n'
