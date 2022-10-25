from cgitb import reset
from logging import Logger

from slack_bolt import Ack, Say
from slack_sdk import WebClient

from app.gql.graph_ql_service import GraphQLService
from app.gql.user_query import insertUserMutationStr

from app.blocks.you_are_on_break_message import you_are_on_break


def kilo_break_action(ack: Ack, client: WebClient, body: dict, say: Say, logger: Logger):

    ack()

    user_id = body["user"]["id"]
    user_info = client.users_info(user=user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

    client.chat_postMessage(
        channel="#attendance-beta",
        blocks=you_are_on_break(name, '5 min')
    )

    trigger_id = body['trigger_id']
    

    # say(
    #     channel='#attendance-beta',
    #     text='''{
    #         "response_action": "clear"
    #     }''')

    # full_name = state["full_name"]["plain_text_input-action"]["value"]
    # email = state["email"]["plain_text_input-action"]["value"]
    # phone = state["phone"]["plain_text_input-action"]["value"]
    # title = state["title"]["plain_text_input-action"]["value"]

    # print({
    #     "Full name": full_name,
    #     "Email": email,
    #     "Phone": phone,
    #     "Title": title
    # })


# v = {'type': 'block_actions', 'user': {'id': 'U02NVERT65B', 'username': 'shkhnk', 'name': 'shkhnk', 'team_id': 'T02NRMZN8NS'}, 'api_app_id': 'A041B86RPKK', 'token': 'WhZeL8jaksq091eEOcIbXt8Z', 'container': {'type': 'view', 'view_id': 'V046P4CRBGE'}, 'trigger_id': '4230807825301.2773747756774.63cbe6247440602769fa61cf8458a55a', 'team': {'id': 'T02NRMZN8NS', 'domain': 'carbonanik'}, 'enterprise': None, 'is_enterprise_install': False, 'view': {'id': 'V046P4CRBGE', 'team_id': 'T02NRMZN8NS', 'type': 'modal', 'blocks': [{'type': 'section', 'block_id': 'ruAIu', 'text': {'type': 'mrkdwn', 'text': ':white_check_mark: *Seletc a break you need*', 'verbatim': False}}, {'type': 'section', 'block_id': '9cK', 'text': {'type': 'mrkdwn', 'text': '*:coffee:Kilo Break*', 'verbatim': False}, 'accessory': {'type': 'button', 'action_id': 'kilo-break', 'style': 'primary', 'text': {'type': 'plain_text', 'text': '5 min', 'emoji': True}, 'value': 'kilo-break'}}, {'type': 'section', 'block_id': '0C3qy', 'text': {'type': 'mrkdwn', 'text': '*:sleeping_accommodation:Mega Break*', 'verbatim': False}, 'accessory': {
#     'type': 'button', 'action_id': 'mega-break', 'style': 'primary', 'text': {'type': 'plain_text', 'text': '10 min', 'emoji': True}, 'value': 'mega-break'}}, {'type': 'section', 'block_id': 'izfnP', 'text': {'type': 'mrkdwn', 'text': '*:beach_with_umbrella:Giga Break*', 'verbatim': False}, 'accessory': {'type': 'button', 'action_id': 'giga-break', 'style': 'primary', 'text': {'type': 'plain_text', 'text': '20 min', 'emoji': True}, 'value': 'giga-break'}}], 'private_metadata': '', 'callback_id': '', 'state': {'values': {}}, 'hash': '1666029808.YCcUm7rQ', 'title': {'type': 'plain_text', 'text': 'Take a break', 'emoji': True}, 'clear_on_close': False, 'notify_on_close': False, 'close': None, 'submit': None, 'previous_view_id': None, 'root_view_id': 'V046P4CRBGE', 'app_id': 'A041B86RPKK', 'external_id': '', 'app_installed_team_id': 'T02NRMZN8NS', 'bot_id': 'B040S4K565C'}, 'actions': [{'action_id': 'kilo-break', 'block_id': '9cK', 'text': {'type': 'plain_text', 'text': '5 min', 'emoji': True}, 'value': 'kilo-break', 'style': 'primary', 'type': 'button', 'action_ts': '1666029810.579941'}]}
