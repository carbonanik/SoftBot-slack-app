from typing import List
from app.blocks.block.block import header, mrkdwn_text, divider


def you_are_in(name, time, tasks):
    return [
        header(f'{name} In 🕘 {time}'),
        mrkdwn_text(_list_to_task_string(tasks)),
        divider()
    ]


def _list_to_task_string(tasks: List):
    return '*Working on*\n\n' + ''.join([f'🎯 {t} \n' for t in tasks])
