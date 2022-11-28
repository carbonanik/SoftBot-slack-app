from slack_bolt import App

from app.listeners.messages.back_message import back_message
from app.listeners.messages.break_message import break_message
from app.listeners.messages.sample_message_callback import sample_message_callback
from app.listeners.messages.in_message import in_message
from app.listeners.messages.in_attendance_to_google_spread_sheet import in_attendance_to_google_spread_sheet
from app.listeners.messages.test_message import test_message
from app.listeners.messages.start_message import start_message
from app.listeners.messages.out_message import out_message
from app.listeners.messages.summery_message import summery_message


def register(app: App):
    app.message("test")(test_message)
    app.message("start")(start_message)
    app.message("in")(in_message)
    app.message("out")(out_message)
    app.message("summery")(summery_message)
    app.message("break")(break_message)
    app.message("back")(back_message)
