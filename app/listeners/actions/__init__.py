from slack_bolt import App
from .join_form_submit_actions import join_form_submit


def register(app: App):
    app.action("submit_join")(join_form_submit)