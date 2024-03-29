from app.blocks.block.block import header, divider, markdown_text, titled_list


def daily_summery(date, present_list, absent_list, delayed_list, project_task):
    blocks = [
        header(text=f'Summery of {date}'),
        divider(),
        header(text="Attendance ✍️"),
        markdown_text(markdown=
                      titled_list(title="Present", emoji="👤", items=present_list) +
                      titled_list(title="", emoji="😞", items=delayed_list) +
                      titled_list(title="Absent", emoji="⛔", items=absent_list)
                      ),
        divider(),
        header(text="Work 🛠️"),
    ]

    for pt in project_task:
        blocks.append(
            markdown_text(
                markdown=titled_list(
                    title=pt['project'],
                    emoji="📝",
                    items=pt['tasks']
                )
            )
        )
    blocks.append(divider())

    return blocks
