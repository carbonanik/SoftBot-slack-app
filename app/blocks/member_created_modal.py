def member_created_modal():
    return {
        "type": "modal",
        "callback_id": "modal-identifier",
        "title": {
                "type": "plain_text",
                "text": "Congratulation! 🎉 "
        },
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*You are now a member* 💕"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Let's assain yourself to a task ? :ghost:*"
                },
                "accessory": {
                    "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Click Here",
                                        "emoji": True
                            },
                    "value": "click_me_123",
                    "action_id": "assain-to-task",
                    "style": "danger"
                }
            }
        ]
    }
