import re

from slack_bolt import App

from app.features.in_feature.actions.select_projects_next import select_projects_next
from app.features.in_feature.message.on_message import on_message


def register_feature_in(app: App):

    # message
    app.message(re.compile("in test", re.IGNORECASE))(on_message)

    # actions
    app.action('select-projects-next')(select_projects_next)
