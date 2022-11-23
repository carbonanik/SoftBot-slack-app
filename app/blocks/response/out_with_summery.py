from app.blocks.block.block import header, divider, mrkdwn_text, titled_list


def out_with_summery(name, time, hour, project, tasks):
    return [
        header(text=f"{name} out at {time}, worked {hour}"),
        mrkdwn_text(
            markdown=titled_list(
                title=project,
                emoji="📝",
                items=tasks
            )
        ),
        divider()
    ]
