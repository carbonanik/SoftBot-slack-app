from app.blocks.block.block import header, actions, checkbox_element, button_element


def select_projects(projects_array_of_dict):
    return [
        header(text="Select the project And task under it"),
        actions(
            elements=[
                checkbox_element(action_id="project-selected", options=projects_array_of_dict),
                button_element(text="Next", value="start", action_id="select-projects-next")
            ],
            block_id="select-project"),
    ]
