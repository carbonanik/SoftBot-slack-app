from app.blocks.block.block import header
from app.blocks.modals.modal_template import modal_template


def loading_modal():
    return modal_template(
        title="Please Wait 🐌 ",
        blocks=[
            header(text="Loading... 🤔")
        ]
    )
