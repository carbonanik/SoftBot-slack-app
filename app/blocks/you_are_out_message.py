def you_are_out(name, date, time, task, working):
    return [
        {
            "type": "header",
            "text": {
                    "type": "plain_text",
                    "text": "Your are Out",
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
                },
				{
					"type": "mrkdwn",
					"text": f"*Working:*\n{working}"
				}
            ]
        },
        {
            "type": "divider"
        }
    ]
