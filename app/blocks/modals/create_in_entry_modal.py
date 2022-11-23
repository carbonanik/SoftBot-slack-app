from app.blocks.modals.modal_template import modal_template
from app.blocks.block.block import multiline_text_input, context_text


def create_in_entry_modal():
    return modal_template(
        title="Start Here 📝",
        submit="Start",
        close="Cancel",
        blocks=[
            multiline_text_input(
                label="✏️ Write down today's tasks.",
                placeholder="Enter Task Title",
                block_id="task_name",
                action_id="plain_text_input-action"
            ),
            context_text("Separate task using comma,")
        ],
        callback_id="create_in_entry",
    )