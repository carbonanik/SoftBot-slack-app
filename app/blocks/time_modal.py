def time_modal():
    return {
        "title": {
            "type": "plain_text",
                    "text": "Start Here 📝"
        },
        "submit": {
            "type": "plain_text",
                    "text": "Start"
        },
        "close": {
            "type": "plain_text",
                    "text": "Cancel"
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "<!date^1666026600^Posted {date_num} {time_secs}|Posted 2014-02-18 5:07:00 PM>"
                }
            }
        ]
    }
