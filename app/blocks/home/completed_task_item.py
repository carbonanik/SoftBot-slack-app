def completed_task_item(title, description):
    return [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*" + title + "*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": description,
                "emoji": True
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Completed",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "style": "primary"
                }
            ]
        },
        {
            "type": "divider"
        },
    ]
