from app.blocks.block.block import header, divider


def team_are_on_break(break_time):
    return [
        header(f'👥 Team On {break_time}️'),
        divider()
    ]
