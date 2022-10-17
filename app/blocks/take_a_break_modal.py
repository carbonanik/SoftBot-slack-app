def take_a_break_modal():
    return {
        "title": {
            "type": "plain_text",
            "text": "Take a break",
            "emoji": True
        },
        "type": "modal",
        "blocks": [
                {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": "✅ *Seletc a break you need*"
                    }
                },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": "*☕Kilo Break*"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "5 min",
                                        "emoji": True
                        },
                        "style": "primary",
                        "value": "click_me_123"
                    }
            },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": "*🛌Mega Break*"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "10 min",
                                        "emoji": True
                        },
                        "style": "primary",
                        "value": "click_me_123"
                    }
            },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": "*🏖️Giga Break*"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "20 min",
                                        "emoji": True
                        },
                        "style": "primary",
                        "value": "click_me_123"
                    }
            }
        ]
    }
