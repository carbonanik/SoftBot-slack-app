from pydoc import cli
from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from service_account import wks
from app.util.date_time import now_date_str, now_time_str
from app.blocks.you_are_in_message import you_are_in
from app.util.const import loacl_date_col, us_date_col , col_letter,in_local_time_col,in_us_time_col, name_col, slack_id_col, working_on_col


def create_in_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]

    print(client.channels_info)
    print(body)

    task_name = state["task_name"]["plain_text_input-action"]["value"]

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
    local_tz = user_info['tz']
    us_eastern_tz = 'US/Eastern'

    build_row = [None] * 20
    build_row.insert(name_col, name)
    build_row.insert(slack_id_col, slack_user_id)
    build_row.insert(working_on_col, task_name)

    wks.insert_row(build_row, index=2)
    wks.update(f'{col_letter[loacl_date_col]}2', now_date_str(local_tz), raw=False)
    wks.update(f'{col_letter[us_date_col]}2', now_date_str(us_eastern_tz), raw=False)
    wks.update(f'{col_letter[in_local_time_col]}2', now_time_str(local_tz), raw=False)
    wks.update(f'{col_letter[in_us_time_col]}2', now_time_str(us_eastern_tz), raw=False)

    client.chat_postMessage(
        channel="#attendance-beta",
        blocks=you_are_in(
            name=name, 
            date=now_date_str(local_tz),
            task=task_name, 
            time=now_time_str(local_tz)
        )
    )

{'type': 'view_submission', 'team': {'id': 'T02NRMZN8NS', 'domain': 'carbonanik'}, 'user': {'id': 'U02NVERT65B', 'username': 'shkhnk', 'name': 'shkhnk', 'team_id': 'T02NRMZN8NS'}, 'api_app_id': 'A041B86RPKK', 'token': 'WhZeL8jaksq091eEOcIbXt8Z', 'trigger_id': '4266844239157.2773747756774.500a9f8275ba9782e2bfea1c42952f8a', 'view': {'id': 'V047UQTS2PP', 'team_id': 'T02NRMZN8NS', 'type': 'modal', 'blocks': [{'type': 'input', 'block_id': 'task_name', 'label': {'type': 'plain_text', 'text': '✏️ What will you wark on now?', 'emoji': True}, 'optional': False, 'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'placeholder': {'type': 'plain_text', 'text': 'Enter Task Title', 'emoji': True}, 'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}}], 'private_metadata': '', 'callback_id': 'create_in_entry', 'state': {'values': {'task_name': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'channl viw'}}}}, 'hash': '1666676753.6Pqu8pmX', 'title': {'type': 'plain_text', 'text': 'Start Here :memo:', 'emoji': True}, 'clear_on_close': False, 'notify_on_close': False, 'close': {'type': 'plain_text', 'text': 'Cancel', 'emoji': True}, 'submit': {'type': 'plain_text', 'text': 'Start', 'emoji': True}, 'previous_view_id': None, 'root_view_id': 'V047UQTS2PP', 'app_id': 'A041B86RPKK', 'external_id': '', 'app_installed_team_id': 'T02NRMZN8NS', 'bot_id': 'B040S4K565C'}, 'response_urls': [], 'is_enterprise_install': False, 'enterprise': None}