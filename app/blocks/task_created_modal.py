def task_created_modal():
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
                    "text": "*You have created a new Task* 💕"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Start working on the task ? :ghost:*"
                },
                "accessory": {
                    "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Assain",
                                        "emoji": True
                            },
                    "value": "click_me_123",
                    "action_id": "assain-to-task",
                    "style": "danger"
                }
            }
        ]
    }