import json

ob = {'type': 'block_actions', 'user': {'id': 'U02NVERT65B', 'username': 'shkhnk', 'name': 'shkhnk', 'team_id': 'T02NRMZN8NS'}, 'api_app_id': 'A041B86RPKK', 'token': 'WhZeL8jaksq091eEOcIbXt8Z', 'container': {'type': 'message', 'message_ts': '1669632450.570649', 'channel_id': 'D040YNFKT7U', 'is_ephemeral': False}, 'trigger_id': '4428673882373.2773747756774.e98ffca9852f47a06feab2e14aad7b29', 'team': {'id': 'T02NRMZN8NS', 'domain': 'carbonanik'}, 'enterprise': None, 'is_enterprise_install': False, 'channel': {'id': 'D040YNFKT7U', 'name': 'directmessage'}, 'message': {'bot_id': 'B040S4K565C', 'type': 'message', 'text': "This content can't be displayed.", 'user': 'U040J5JEFSB', 'ts': '1669632450.570649', 'app_id': 'A041B86RPKK', 'blocks': [{'type': 'header', 'block_id': 'umJ', 'text': {'type': 'plain_text', 'text': 'Add new project :orange_book:', 'emoji': True}}, {'type': 'input', 'block_id': 'project-name', 'label': {'type': 'plain_text', 'text': 'Project Name ', 'emoji': True}, 'optional': False, 'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}}, {'type': 'input', 'block_id': 'project-description', 'label': {'type': 'plain_text', 'text': 'Description ', 'emoji': True}, 'optional': False, 'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'placeholder': {'type': 'plain_text', 'text': 'Write a short description of the project', 'emoji': True}, 'multiline': True, 'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}}, {'type': 'actions', 'block_id': 'create-project', 'elements': [{'type': 'button', 'action_id': 'create-project', 'text': {'type': 'plain_text', 'text': 'Create', 'emoji': True}, 'style': 'danger', 'value': '0'}]}], 'team': 'T02NRMZN8NS'}, 'state': {'values': {'project-name': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'py'}}, 'project-description': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'py d'}}}}, 'response_url': 'https://hooks.slack.com/actions/T02NRMZN8NS/4444258705361/Ai7bsQ6oIBJOYtUl6x9EcPlB', 'actions': [{'action_id': 'create-project', 'block_id': 'create-project', 'text': {'type': 'plain_text', 'text': 'Create', 'emoji': True}, 'value': '0', 'style': 'danger', 'type': 'button', 'action_ts': '1669632461.008926'}]}


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr


jstr = convert_obj(ob)

text_file = open("data.json", "w")

text_file.write(jstr)
# print(text_file.read())

text_file.close()
