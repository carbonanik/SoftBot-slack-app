from app.blocks.block.block import header, markdown_text, text_option, actions, checkbox_element, button_element, \
    plain_text_input


def add_and_select_task_blocks(project, tasks, hack_for_project_id):
    blocks = [
        header(text=project),
        markdown_text(markdown="Select the task you want to work on") if tasks else None,
        actions(
            elements=[
                checkbox_element(action_id="task-selected", options=tasks, initial_options=tasks),
                button_element(text="Start", value="start", action_id="start-selected-tasks")
            ],
            block_id="select-tasks") if tasks else None,
        plain_text_input(action_id="plain_text_input-action", text="New Task Name", block_id="task-name"),
        actions(elements=[
            button_element(text="Add Task", value=hack_for_project_id, action_id="add-task", style="danger")
        ], block_id="add-task"),
    ]

    def remove_none(b):
        return True if b else False

    return list(filter(remove_none, blocks))

