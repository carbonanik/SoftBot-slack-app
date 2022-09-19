def already_joined_modal():
    return {
        "type": "modal",
        "callback_id": "modal-identifier",
        "title": {
                "type": "plain_text",
                "text": "Welcome! 🚀 "
        },
        "blocks": [
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
            }
        ]
    }
