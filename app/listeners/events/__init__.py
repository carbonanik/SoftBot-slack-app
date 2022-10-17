
import imp
from slack_bolt import App
from .app_home_opened_callback import app_home_opened_callback
from .join_form_madal_submit_event import join_form_madal_submit_event
from .create_task_modal_submit_event import create_task_madal_submit_event
from .create_in_entry_submit import create_in_submit_event
from .take_a_break_submit_event import take_a_break_submit_event

def register(app: App):
    app.event("app_home_opened")(app_home_opened_callback) 
    app.view("join_form")(join_form_madal_submit_event)
    app.view("create_task")(create_task_madal_submit_event)
    app.view("create_in_entry")(create_in_submit_event)
    app.view("take_a_break")(take_a_break_submit_event)
