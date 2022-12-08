from app.blocks.block.block import markdown_text, actions, checkbox_element, header, plain_text_input, button_element


def select_task_under_project_and_add_task_blocks(project_task_dict):
    blocks = []

    projects_id_payload = ','.join(map(lambda p: p['value'], project_task_dict))
    projects_name = list(map(lambda p: p['project'], project_task_dict))

    if len(project_task_dict) > 1:
        projects_payload = ', '.join(projects_name[:-1]) + ' & ' + projects_name[-1]
    else:
        projects_payload = projects_name[0]

    for pd in project_task_dict:
        blocks.append(
            header(text=pd['project'])
        )

        if pd['tasks']:
            blocks.append(actions(elements=[
                checkbox_element(
                    action_id='task-under-project-selected',
                    options=pd['tasks']
                )
            ], block_id=f'task-under-project-{pd["value"]}'))

        blocks.append(
            plain_text_input(
                action_id="plain_text_input-action",
                text="New Task Name",
                block_id=f"task-name-{pd['value']}"
            ),
        )
        blocks.append(
            actions(elements=[
                button_element(text="Add Task", value=projects_id_payload, action_id="add-task", style="danger")
            ], block_id=f"add-task-{pd['value']}"),
        )

    blocks.append(actions(elements=[
        button_element(
            text="Start",
            value=projects_payload,
            action_id="start-selected-task-in-multiple-project"
        )
    ], block_id=f"start-tasks"))

    return blocks
