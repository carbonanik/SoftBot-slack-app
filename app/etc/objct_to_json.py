import json


ob = {'type': 'block_actions', 'user': {'id': 'U02NVERT65B', 'username': 'shkhnk', 'name': 'shkhnk', 'team_id': 'T02NRMZN8NS'}, 'api_app_id': 'A041B86RPKK', 'token': 'WhZeL8jaksq091eEOcIbXt8Z', 'container': {'type': 'message', 'message_ts': '1668059150.926379', 'channel_id': 'C047Z9D3ADQ', 'is_ephemeral': False}, 'trigger_id': '4350704704530.2773747756774.4a848f7a9e987905b8476fcf869c384b', 'team': {'id': 'T02NRMZN8NS', 'domain': 'carbonanik'}, 'enterprise': None, 'is_enterprise_install': False, 'channel': {'id': 'C047Z9D3ADQ', 'name': 'attendance-beta'}, 'message': {'bot_id': 'B040S4K565C', 'type': 'message', 'text': "This content can't be displayed.", 'user': 'U040J5JEFSB', 'ts': '1668059150.926379', 'app_id': 'A041B86RPKK', 'blocks': [{'type': 'header', 'block_id': 'y4hYa', 'text': {'type': 'plain_text', 'text': 'Write your feedback on completed task', 'emoji': True}}, {'type': 'input', 'block_id': 'task-1', 'label': {'type': 'plain_text', 'text': 'bea Review', 'emoji': True}, 'optional': False, 'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}}, {'type': 'input', 'block_id': 'task-2', 'label': {'type': 'plain_text', 'text': 'baba Review', 'emoji': True}, 'optional': False, 'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}}, {'type': 'header', 'block_id': '8YPCs', 'text': {'type': 'plain_text', 'text': 'Write down the blockers :construction: for', 'emoji': True}}, {'type': 'input', 'block_id': 'project-1', 'label': {'type': 'plain_text', 'text': 'Project 1 Blockers', 'emoji': True}, 'optional': False, 'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}}, {'type': 'actions', 'block_id': 'review-blockers-submit', 'elements': [{'type': 'button', 'action_id': 'review-blockers-submit', 'text': {'type': 'plain_text', 'text': ':radio_button: Submit', 'emoji': True}, 'style': 'primary', 'value': 'submit'}]}], 'team': 'T02NRMZN8NS', 'edited': {'user': 'B040S4K565C', 'ts': '1668059159.000000'}}, 'state': {'values': {'task-1': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'bea review good'}}, 'task-2': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'baba review bad'}}, 'project-1': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'project 1 big blocker'}}}}, 'response_url': 'https://hooks.slack.com/actions/T02NRMZN8NS/4336168478279/u99VMqdgKVee4VqjziLPKudd', 'actions': [{'action_id': 'review-blockers-submit', 'block_id': 'review-blockers-submit', 'text': {'type': 'plain_text', 'text': ':radio_button: Submit', 'emoji': True}, 'value': 'submit', 'style': 'primary', 'type': 'button', 'action_ts': '1668059246.206166'}]}


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr

jstr = convert_obj(ob)


text_file = open("data.json", "w")

text_file.write(jstr)
# print(text_file.read())
 
text_file.close()