from typing import List
from app.blocks.block.block import header, markdown_text, divider


def you_are_in(name, time, project, tasks):
    return [
        header(f'{name} In 🕘 {time}'),
        markdown_text(_list_to_task_string(tasks, project)),
        divider()
    ]


def _list_to_task_string(tasks: List, project):
    return f'Working on *{project}*\n' + ''.join([f'🎯 {t} \n' for t in tasks])
