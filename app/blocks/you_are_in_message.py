def you_are_in(name, date, time, task):
    return [
        {
            "type": "header",
            "text": {
                    "type": "plain_text",
                    "text": "Your are In",
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
                    "text": f"*Task:*\n{task}"
                }

            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*Time:*\n{time}"
                },  
                {
                    "type": "mrkdwn",
                    "text": f"*Date:*\n{date}"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]
