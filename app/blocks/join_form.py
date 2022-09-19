
def join_form(name="", email="", phone="", title=""):
    return [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Joint Attendance 🏫🏫",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": "full_name",
            "element": {
                "type": "plain_text_input",
                "action_id": "plain_text_input-action",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter Your Full Name"
                },
                "initial_value": name
            },
            "label": {
                "type": "plain_text",
                "text": "Full Name",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": "email",
            "element": {
                "type": "plain_text_input",
                "action_id": "plain_text_input-action",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter Your Email Address"
                },
                "initial_value": email
            },
            "label": {
                "type": "plain_text",
                "text": "Email",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": "phone",
            "element": {
                "type": "plain_text_input",
                "action_id": "plain_text_input-action",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter Your Phone Number"
                },
                "initial_value": phone
            },
            "label": {
                "type": "plain_text",
                "text": "Phone",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": "title",
            "element": {
                "type": "plain_text_input",
                "action_id": "plain_text_input-action",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter Your Job Title"
                },
                "initial_value": title
            },
            "label": {
                "type": "plain_text",
                "text": "Title",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Fill up the form to join.",
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
                        "text": "Submit",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "submit_join",
                    "style": "primary",
                }
            ]
        },
        {
            "type": "divider"
        }
    ]

