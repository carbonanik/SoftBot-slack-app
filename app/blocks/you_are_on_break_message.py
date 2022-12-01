def you_are_on_break(name, duration):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Your are on Break",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*Name:*\n{name}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Duration:*\n{duration}"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]
