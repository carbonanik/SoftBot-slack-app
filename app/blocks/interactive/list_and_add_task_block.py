from app.blocks.block.block import header, markdown_text, text_option, actions, checkbox_element, button_element, \
    plain_text_input, titled_list


def list_and_add_task_block(project, tasks, hack_for_project_id):
    blocks = [
        # header(text=project),
        markdown_text(
            markdown=titled_list(
                title=f"📝️List of all task from project {project}",
                emoji="🛠️",
                items=tasks
            )
        ),

        plain_text_input(
            action_id="plain_text_input-action",
            text="New Task Name",
            block_id="task-name"
        ),

        actions(
            elements=[
                button_element(
                    text="Add Task",
                    value=hack_for_project_id,
                    action_id="only-add-task",
                    style="danger"
                )
            ],
            block_id="add-task"
        ),
    ]

    def remove_none(b):
        return True if b else False

    return list(filter(remove_none, blocks))
