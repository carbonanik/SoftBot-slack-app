from typing import List

from app.blocks.block.block import header, markdown_text


def you_are_out(name, duration, tasks):
    return [
        header(text=f'{name} out 🧭 {duration}'),
        markdown_text(markdown=_list_to_task_string(tasks=tasks))
    ]


def _list_to_task_string(tasks: List):
    return ''.join([f'✅ {t} \n' for t in tasks])
