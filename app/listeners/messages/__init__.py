import re
from slack_bolt import App

from app.listeners.messages.sample_message_callback import sample_message_callback
from app.listeners.messages.in_attendance import in_attendance
from app.listeners.messages.in_attendance_to_google_spread_sheet import in_attendance_to_google_spread_sheet

def register(app: App):
    app.message(re.compile("(hi|hello|hey)"))(sample_message_callback)
    # app.message(re.compile("in"))(in_attendance_to_google_spread_sheet)
    # app.message(re.compile("in [\w| ]+"))(in_attendance)
    