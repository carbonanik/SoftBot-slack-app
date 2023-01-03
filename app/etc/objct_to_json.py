import json

ob = {'type': 'block_actions',
      'user': {'id': 'U02NVERT65B', 'username': 'shkhnk', 'name': 'shkhnk', 'team_id': 'T02NRMZN8NS'},
      'api_app_id': 'A041B86RPKK', 'token': 'WhZeL8jaksq091eEOcIbXt8Z',
      'container': {'type': 'message', 'message_ts': '1670427915.569379', 'channel_id': 'D040YNFKT7U',
                    'is_ephemeral': False},
      'trigger_id': '4494688031665.2773747756774.025fc6194bf87018c6f15490bde41abf',
      'team': {'id': 'T02NRMZN8NS', 'domain': 'carbonanik'}, 'enterprise': None, 'is_enterprise_install': False,
      'channel': {'id': 'D040YNFKT7U', 'name': 'directmessage'},
      'message': {'bot_id': 'B040S4K565C', 'type': 'message', 'text': "This content can't be displayed.",
                  'user': 'U040J5JEFSB', 'ts': '1670427915.569379', 'app_id': 'A041B86RPKK', 'blocks': [
              {'type': 'header', 'block_id': 'ewnfK', 'text': {'type': 'plain_text', 'text': 'py', 'emoji': True}},
              {'type': 'input', 'block_id': 'task-name-10',
               'label': {'type': 'plain_text', 'text': 'New Task Name', 'emoji': True}, 'optional': False,
               'dispatch_action': False,
               'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'initial_value': '',
                           'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}},
              {'type': 'actions', 'block_id': 'add-task-10', 'elements': [{'type': 'button', 'action_id': 'add-task',
                                                                           'text': {'type': 'plain_text',
                                                                                    'text': 'Add Task', 'emoji': True},
                                                                           'style': 'danger', 'value': 'add'}]},
              {'type': 'header', 'block_id': 'Z9rR', 'text': {'type': 'plain_text', 'text': 'War lock', 'emoji': True}},
              {'type': 'input', 'block_id': 'task-name-11',
               'label': {'type': 'plain_text', 'text': 'New Task Name', 'emoji': True}, 'optional': False,
               'dispatch_action': False,
               'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action', 'initial_value': '',
                           'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}}},
              {'type': 'actions', 'block_id': 'add-task-11', 'elements': [{'type': 'button', 'action_id': 'add-task',
                                                                           'text': {'type': 'plain_text',
                                                                                    'text': 'Add Task', 'emoji': True},
                                                                           'style': 'danger', 'value': 'add'}]}],
                  'team': 'T02NRMZN8NS', 'edited': {'user': 'B040S4K565C', 'ts': '1670427919.000000'}},
      'state': {'values': {'task-name-10': {'plain_text_input-action': {'type': 'plain_text_input', 'value': 'New'}}}},
      'response_url': 'https://hooks.slack.com/actions/T02NRMZN8NS/4479103842661/YfcIqphb9G8SFoD32pQqOcdI', 'actions': [
        {'action_id': 'add-task', 'block_id': 'add-task-10',
         'text': {'type': 'plain_text', 'text': 'Add Task', 'emoji': True}, 'value': 'add', 'style': 'danger',
         'type': 'button', 'action_ts': '1670427927.609946'}]}


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr


jstr = convert_obj(ob)

text_file = open("data.json", "w")

text_file.write(jstr)
# print(text_file.read())

text_file.close()
