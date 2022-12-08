from app.blocks.block.block import header, markdown_text, text_option, actions, checkbox_element, button_element, \
    plain_text_input


def select_multiple_project_blocks(projects):
    blocks = [
        header(text="Select the project And task under it"),
        actions(
            elements=[
                checkbox_element(action_id="project-selected", options=projects),
                button_element(text="Next", value="start", action_id="selected-project-next")
            ],
            block_id="select-project") if projects else None,
    ]

    def remove_none(b):
        return True if b else False

    return list(filter(remove_none, blocks))
