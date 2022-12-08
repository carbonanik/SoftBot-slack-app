import re

from slack_bolt import App

from app.listeners.messages.add_project_message import add_project_message
from app.listeners.messages.add_task_message import add_task_message
from app.listeners.messages.back_message import back_message
from app.listeners.messages.blockers_message import blockers_message
from app.listeners.messages.break_message import break_message
from app.listeners.messages.in_message import in_message
from app.listeners.messages.out_message import out_message
from app.listeners.messages.start_message import start_message
from app.listeners.messages.summary_message import summary_massage


def register(app: App):
    app.message(re.compile("start", re.IGNORECASE))(start_message)
    app.message(re.compile("in", re.IGNORECASE))(in_message)
    app.message(re.compile("out", re.IGNORECASE))(out_message)
    app.message(re.compile("summary", re.IGNORECASE))(summary_massage)
    app.message(re.compile("break", re.IGNORECASE))(break_message)
    app.message(re.compile("back", re.IGNORECASE))(back_message)
    app.message(re.compile("add project", re.IGNORECASE))(add_project_message)
    app.message(re.compile("blocker", re.IGNORECASE))(blockers_message)
    app.message(re.compile("add task", re.IGNORECASE))(add_task_message)
