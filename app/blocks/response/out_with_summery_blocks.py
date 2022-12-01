from app.blocks.block.block import header, divider, markdown_text, titled_list


def out_with_summery_blocks(name, time, hour, project, tasks):
    return [
        header(text=f"{name} out at {time}, worked {hour}"),
        markdown_text(
            markdown=titled_list(
                title=project,
                emoji="📝",
                items=tasks
            )
        ),
        divider()
    ]
