from app.blocks.block.block import header, divider, markdown_text, titled_list


def project_blockers_blocks(project_blockers):
    blocks = [header(text="Blockers 🚧️")]

    for pb in project_blockers:
        blocks.append(
            markdown_text(
                markdown=titled_list(
                    title=pb['project'],
                    emoji="📝",
                    items=pb['blocker']
                )
            )
        )
    blocks.append(divider())

    return blocks
