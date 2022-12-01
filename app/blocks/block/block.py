from typing import List


def header(text: str) -> dict:
    return {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": text,
            "emoji": True
        }
    }


def divider() -> dict:
    return {
        "type": "divider"
    }


def markdown_text(markdown: str) -> dict:
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": markdown
        }
    }


def context_text(text: str) -> dict:
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


def multiline_text_input(
        label: str,
        placeholder: str,
        block_id: str,
        action_id: str
) -> dict:
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
