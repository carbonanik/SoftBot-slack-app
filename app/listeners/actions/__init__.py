from slack_bolt import App
from .join_form_submit_actions import join_form_submit
from .kilo_break_action import kilo_break_action
from .mega_break_action import mega_break_action
from .giga_break_action import giga_break_action


def register(app: App):
    app.action("submit_join")(join_form_submit)
    app.action("kilo-break")(kilo_break_action)
    app.action("mega-break")(mega_break_action)
    app.action("giga-break")(giga_break_action)