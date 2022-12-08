from app.blocks.block.block import header
from app.blocks.interactive.and_and_select_task_blocks import plain_text_input, actions, button_element


def review_and_blockers_blocks(tasks, project, projects_ids):
    blocks = [header("Write your feedback on completed task")]

    blocks += [plain_text_input(
        action_id="plain_text_input-action",
        text=f'{task["text"]} Review',
        block_id=f'task-{task["value"]["task_id"]}'
    ) for task in tasks]

    if project:
        blocks.append(
            header("Write down the blockers 🚧 for")
        )
        blocks.append(
            plain_text_input(
                action_id="plain_text_input-action",
                text=f"{project['title']} Blockers",
                block_id=f"project-{project['id']}"
            )
        )
    blocks.append(
        actions(elements=[
            button_element(text="🔘 Submit", value=projects_ids, action_id="review-blockers-submit")
        ], block_id="review-blockers-submit")
    )
    return blocks
