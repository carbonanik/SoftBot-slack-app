from app.blocks.block.block import radio_button_select


def select_individual_break():
    return [
        radio_button_select(
            block_id="individual_break_radio",
            action_id="individual_break_select",
            label="✅ Seletc a break you need",
            options=[
                {"text": "30 minutes break ☕", "value": "1"},
                {"text": "1 hour break 🍔️", "value": "2"},
                {"text": "2 hours break 🛏", "value": "3"},
                {"text": "4 hours break 🏖️", "value": "4"},
            ]
        ),
    ]
