def create_in_entry_modal():
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
			"type": "input",
			"block_id": "task_name",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action",
				"placeholder": {
					"type": "plain_text",
					"text": "Enter Task Title"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "✏️ What will you wark on now?",
				"emoji": True
			}
		}
	],
	"type": "modal",
	"callback_id": "create_in_entry"
}