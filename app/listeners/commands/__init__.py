from slack_bolt import App

from .join_attendance import join_attendance
from .create_task import create_task
from .in_command import in_command
from .out_command import out_command
from .break_command import break_command
from .back_command import back_command
from .team_break_command import team_break_command
from .team_back_command import team_back_command
from .daily_summery_command import daily_summery_command


def register(app: App):
    app.command("/add-task")(create_task)
    app.command("/in")(in_command)
    app.command("/out")(out_command)
    app.command("/break")(break_command)
    app.command("/back")(back_command)
    app.command("/team-break")(team_break_command)
    app.command("/team-back")(team_back_command)
    app.command("/summery")(daily_summery_command)
