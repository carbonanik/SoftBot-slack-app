def create_task_modal(date):
    return {
        "title": {
            "type": "plain_text",
            "text": "Create Task 📝"
        },
        "submit": {
            "type": "plain_text",
            "text": "Create"
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
                        "text": "Enter Task Name"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "✏️ Task Name",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "description",
                "optional": True,
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Write Something About The Task"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "🗒️ Description",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "block_id": "deadline",
                "text": {
                    "type": "mrkdwn",
                    "text": "*📅 Pick a date for the deadline.*"
                },
                "accessory": {
                    "type": "datepicker",
                    "initial_date": date,#"1990-04-28"
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    },
                    "action_id": "datepicker-action"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Create New Task* :ghost:"
                }
            }
        ],
        "type": "modal",
        "callback_id": "create_task"
    }
