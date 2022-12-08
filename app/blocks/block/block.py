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
    if title:
        title = f'*{title}*\n'
    return title + ''.join([f'{emoji} {item} \n' for item in items]) + '\n'


def actions(elements, block_id):
    return {
        "type": "actions",
        "elements": elements,
        "block_id": block_id,
    }


def button_element(text, value, action_id, style="primary"):
    return {
        "type": "button",
        "style": style,
        "text": {
            "type": "plain_text",
            "text": text
        },
        "value": value,
        "action_id": action_id
    }


def plain_text_input(text, action_id, block_id, initial_value=""):
    return {
        "type": "input",
        "block_id": block_id,
        "element": {
            "type": "plain_text_input",
            "action_id": action_id,
            "initial_value": initial_value
        },
        "label": {
            "type": "plain_text",
            "text": text,
            "emoji": True
        }
    }


def checkbox_element(options, action_id, initial_options=None):
    return {
        "type": "checkboxes",
        "options": [text_option(text=option["text"], value=option["value"]) for option in options],
        # "initial_options": [text_option(text=option["text"], value=option["value"]) for option in
        #                     initial_options],
        "action_id": action_id
    }
