import json

ob = {'type': 'block_actions',
      'user': {'id': 'U03N9KY285A', 'username': 'shkhnk', 'name': 'shkhnk', 'team_id': 'T032R570L6S'},
      'api_app_id': 'A047XH9UFA6', 'token': 'TcMRHsBsKbewEYqI8zUnmqZr',
      'container': {'type': 'message', 'message_ts': '1669210374.857219', 'channel_id': 'D048M93Q6KS',
                    'is_ephemeral': False},
      'trigger_id': '4400594137687.3093177020230.c305ac4884e8bff7970cb4c566a9df7c',
      'team': {'id': 'T032R570L6S', 'domain': 'klwebco'}, 'enterprise': None, 'is_enterprise_install': False,
      'channel': {'id': 'D048M93Q6KS', 'name': 'directmessage'},
      'message': {'bot_id': 'B047H1UGAP9', 'type': 'message', 'text': "This content can't be displayed.",
                  'user': 'U048A79CNQ1', 'ts': '1669210374.857219', 'app_id': 'A047XH9UFA6', 'blocks': [
              {'type': 'header', 'block_id': 'ENj',
               'text': {'type': 'plain_text', 'text': 'Write your feedback on completed task', 'emoji': True}},
              {'type': 'input', 'block_id': 'task-48',
               'label': {'type': 'plain_text', 'text': 'a Review', 'emoji': True}, 'optional': False,
               'dispatch_action': False, 'element': {'type': 'plain_text_input', 'action_id': 'plain_text_input-action',
                                                     'dispatch_action_config': {
                                                         'trigger_actions_on': ['on_enter_pressed']}}},
              {'type': 'actions', 'block_id': 'review-blockers-submit', 'elements': [
                  {'type': 'button', 'action_id': 'review-blockers-submit',
                   'text': {'type': 'plain_text', 'text': ':radio_button: Submit', 'emoji': True}, 'style': 'primary',
                   'value': 'submit'}]}], 'team': 'T032R570L6S',
                  'edited': {'user': 'B047H1UGAP9', 'ts': '1669210381.000000'}}, 'state': {'values': {}},
      'response_url': 'https://hooks.slack.com/actions/T032R570L6S/4427776132193/3IvFsGfmqkXYhnR0eur1vpZz', 'actions': [
        {'action_id': 'review-blockers-submit', 'block_id': 'review-blockers-submit',
         'text': {'type': 'plain_text', 'text': ':radio_button: Submit', 'emoji': True}, 'value': 'submit',
         'style': 'primary', 'type': 'button', 'action_ts': '1669210601.182587'}]}


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr


jstr = convert_obj(ob)

text_file = open("data.json", "w")

text_file.write(jstr)
# print(text_file.read())

text_file.close()
