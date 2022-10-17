def take_a_break_radio_select_modal():
    return {
	"title": {
		"type": "plain_text",
		"text": "Take a break",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"type": "modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
    "callback_id": "take_a_break",
	"blocks": [
		{
			"type": "input",
			"block_id": "select_break",
			"label": {
				"type": "plain_text",
				"text": "✅ Seletc a break you need",
				"emoji": True
			},
			"element": {
				"type": "radio_buttons",
				"action_id": "options",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "5 min ☕",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "10 min 🛌",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "20 min 🏖️",
							"emoji": True
						},
						"value": "3"
					}
				]
			}
		}
	]
}