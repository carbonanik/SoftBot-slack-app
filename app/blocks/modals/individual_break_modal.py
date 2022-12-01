from app.blocks.modals.modal_template import modal_template
from app.blocks.block.block import radio_button_select, multiline_text_input, context_text


def individual_break_modal():
    return modal_template(
        title="Take a personal break ⛱️",
        submit="Submit",
        close="Cancel",
        blocks=[
            radio_button_select(
                block_id="individual_break_radio",
                action_id="individual_break_select",
                label="✅ Select a break you need",
                options=[
                    {"text": "30 minutes break ☕", "value": "1"},
                    {"text": "1 hour break 🛏️", "value": "2"},
                    {"text": "2 hour emergency break 🚑", "value": "3"},
                ]
            ),
        ],
        callback_id="individual_break_submit",
    )
