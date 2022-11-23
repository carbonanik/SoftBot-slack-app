from app.blocks.block.block import header, text_option
from app.blocks.interactive.select_and_add_task import actions


def select_project(projects):
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
