from app.blocks.block.block import header, text_option
from app.blocks.interactive.and_and_select_task_blocks import actions


def select_project_blocks(projects, action_id):
    radio_buttons = {
        "type": "radio_buttons",
        "action_id": action_id,
        "options": [text_option(text=option["text"], value=option["value"])
                    for option in projects]
    }
    return [
        header("Select the project you are going to work on"),
        actions(
            elements=[radio_buttons],
            block_id="projects-block"
        )
    ]
