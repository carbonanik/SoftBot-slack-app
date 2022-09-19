def join_form_modal(name="", email="", phone="", title=""):
    return {
        "title": {
            "type": "plain_text",
            "text": "Joint Attendance Group 🏫"
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit"
        },
        "blocks": [
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
                            "text": "👤 Full Name",
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
                            "text": "✉️ Email",
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
                            "text": "📱 Phone",
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
                            "text": "🤖 Job Title",
                            "emoji": True
                        }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Fill up the form to join.* :ghost:"
                }
            }
        ],
        "type": "modal",
        "callback_id": "join_form",
    }
