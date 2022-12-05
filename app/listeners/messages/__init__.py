from slack_bolt import App

from app.listeners.messages.add_project_message import add_project_message
from app.listeners.messages.add_task_message import add_task_message
from app.listeners.messages.back_message import back_message
from app.listeners.messages.blockers_message import blockers_message
from app.listeners.messages.break_message import break_message
from app.listeners.messages.sample_message_callback import sample_message_callback
from app.listeners.messages.in_message import in_message
from app.listeners.messages.in_attendance_to_google_spread_sheet import in_attendance_to_google_spread_sheet
from app.listeners.messages.test_message import test_message
from app.listeners.messages.start_message import start_message
from app.listeners.messages.out_message import out_message
from app.listeners.messages.summery_message import summery_message
import re


def register(app: App):
    app.message(re.compile("test", re.IGNORECASE))(test_message)
    app.message(re.compile("start", re.IGNORECASE))(start_message)
    app.message(re.compile("in", re.IGNORECASE))(in_message)
    app.message(re.compile("out", re.IGNORECASE))(out_message)
    app.message(re.compile("summary", re.IGNORECASE))(summery_message)
    app.message(re.compile("break", re.IGNORECASE))(break_message)
    app.message(re.compile("back", re.IGNORECASE))(back_message)
    app.message(re.compile("add project", re.IGNORECASE))(add_project_message)
    app.message(re.compile("blocker", re.IGNORECASE))(blockers_message)
    app.message(re.compile("add task", re.IGNORECASE))(add_task_message)
