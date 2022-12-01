from app.blocks.block.block import header, divider


def you_are_on_break(name, break_time):
    return [
        header(f'{name} On ⏱️ {break_time} break 🏖️'),
        divider()
    ]
