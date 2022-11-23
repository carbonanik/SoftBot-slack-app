from app.blocks.block.block import header, mrkdwn_text, text_option


def select_and_add_task(project, tasks, hack_for_project_id):
    blocks = [
        header(text=project),
        mrkdwn_text(markdown="Select the task you want to wark on") if tasks else None,
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


def actions(elements, block_id):
    return {
        "type": "actions",
        "elements": elements,
        "block_id": block_id,
    }


def button_element(text, value, action_id, style="primary"):
    return {
        "type": "button",
        "style": style,
        "text": {
            "type": "plain_text",
            "text": text
        },
        "value": value,
        "action_id": action_id
    }


def plain_text_input(text, action_id, block_id):
    return {
        "type": "input",
        "block_id": block_id,
        "element": {
            "type": "plain_text_input",
            "action_id": action_id
        },
        "label": {
            "type": "plain_text",
            "text": text,
            "emoji": True
        }
    }


def checkbox_element(options, initial_options, action_id):
    return {
        "type": "checkboxes",
        "options": [text_option(text=option["text"], value=option["value"]) for option in options],
        # "initial_options": [text_option(text=option["text"], value=option["value"]) for option in
        #                     initial_options],
        "action_id": action_id
    }
