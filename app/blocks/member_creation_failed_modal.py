def member_cration_failed_modal():
    return {
        "type": "modal",
        "callback_id": "modal-identifier",
        "title": {
                "type": "plain_text",
                "text": "Error 🛑"
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Member creation failed* 💔"
                }
            }
        ]
    }
