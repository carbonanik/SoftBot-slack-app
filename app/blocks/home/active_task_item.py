def active_task_item():
    return [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*title*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "description",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":ghost: *Someone* is working on this,"
			}
		},
		{
			"type": "divider"
		}
	]