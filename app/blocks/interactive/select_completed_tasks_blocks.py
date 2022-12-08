from app.blocks.block.block import header
from app.blocks.interactive.and_and_select_task_blocks import actions, button_element, checkbox_element


def select_completed_task_blocks(tasks, payload):
    return [
        header(text="Select the task you have completed"),
        actions(
            elements=[
                checkbox_element(action_id="completed-task-select", options=tasks, initial_options=tasks),
                button_element(text="Next", value=payload, action_id="select-completed-task-next")
            ],
            block_id="task-to-mark"
        ),
    ]
