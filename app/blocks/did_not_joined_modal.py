def did_not_joined_madal():
    return {
	"type": "modal",
	"callback_id": "modal-identifier",
	"title": {
		"type": "plain_text",
		"text": "Sorry ! 👉👈 "
	},
	"blocks": [
		{
			"type": "divider"
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "You Did Not Joined to Attendance Group 😞",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Want to Join ? :ghost:*"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Click Here",
					"emoji": True
				},
				"value": "click_me_123",
				"action_id": "create-new-task",
				"style": "danger"
			}
		}
	]
}