def already_joined_message():
    return [
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "You have already joined 💕",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Want to create a new task ? :ghost:*"
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Click Me",
                    "emoji": True
                },
                "value": "click_me_123",
                "action_id": "create-new-task",
                "style": "danger"
            }
        },
        {
            "type": "divider"
        }
    ]
