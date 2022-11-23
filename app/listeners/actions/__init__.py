from slack_bolt import App
from .join_form_submit_actions import join_form_submit
from .test_button_click import test_button_click
from .select_project_action import select_project_action
from .add_task_action import add_task_action
from .task_selected_action import task_selected_action
from .start_selected_tasks_action import start_selected_task_action
from .select_completed_task_next_action import select_completed_task_next_action
from .completed_task_select import completed_task_select
from .review_blockers_submit import review_blockers_submit


def register(app: App):
    app.action("submit_join")(join_form_submit)
    app.action("test-button-click")(test_button_click)
    app.action("select-project")(select_project_action)
    app.action("add-task")(add_task_action)
    app.action("task-selected")(task_selected_action)
    app.action("start-selected-tasks")(start_selected_task_action)
    app.action("select-completed-task-next")(select_completed_task_next_action)
    app.action("completed-task-select")(completed_task_select)
    app.action("review-blockers-submit")(review_blockers_submit)
