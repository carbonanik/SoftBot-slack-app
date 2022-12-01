from app.blocks.block.block import header, text_option
from app.blocks.interactive.and_and_select_task_blocks import actions


def select_project_blocks(projects):
    return [
        header("Select the project you are going to work on"),
        actions(elements=[
            {
                "type": "radio_buttons",
                "action_id": "select-project",
                "options": [text_option(text=option["text"], value=option["value"])
                            for option in projects]
            }
        ], block_id="projects-block")
    ]
