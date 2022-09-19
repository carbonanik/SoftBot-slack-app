def loading_modal():
    return {
        "type": "modal",
        "callback_id": "modal-identifier",
        "title": {
                "type": "plain_text",
                "text": "Please Wait 🐌 "
        },
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Loading... 🤔",
                    "emoji": True
                }
            }
        ]
    }
