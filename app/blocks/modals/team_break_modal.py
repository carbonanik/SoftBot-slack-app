from app.blocks.modals.modal_template import modal_template
from app.blocks.block.block import radio_button_select, multiline_text_input, context_text


def team_break_modal():
    return modal_template(
        title="Select team break 🎃",
        submit="Submit",
        close="Cancel",
        blocks=[
            radio_button_select(
                block_id="team_break_radio",
                action_id="team_break_select",
                label="✅ Select the reason",
                options=[
                    {"text": "⚡ Electricity break", "value": "1"},
                    {"text": "🍲 Launch break️", "value": "2"},
                ]
            ),
        ],
        callback_id="team_break_submit",
    )