from slack_bolt import App

from .join_attendance import join_attendance
from .create_task import create_task
from .in_command import in_command
from .out_command import out_command
from .break_command import break_command


def register(app: App):
    app.command("/join-attendance")(join_attendance)
    app.command("/add-task")(create_task)
    app.command("/in")(in_command)
    app.command("/out")(out_command)
    app.command("/break")(break_command)