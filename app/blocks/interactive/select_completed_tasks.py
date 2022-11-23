from app.blocks.block.block import header
from app.blocks.interactive.select_and_add_task import actions, button_element, checkbox_element


def select_completed_task(tasks, hack_for_project_id):
    return [
        header(text="Select the task you have completed"),
        actions(
            elements=[
                checkbox_element(action_id="completed-task-select", options=tasks, initial_options=tasks),
                button_element(text="Next", value=hack_for_project_id, action_id="select-completed-task-next")
            ],
            block_id="task-to-mark"
        ),
    ]
