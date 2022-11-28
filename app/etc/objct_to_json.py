import json

ob = {'is_enterprise_install': False, 'team_id': 'T02NRMZN8NS', 'user_id': 'U02NVERT65B', 'channel_id': 'D040YNFKT7U', 'token': 'xoxb-2773747756774-4018188491895-R1b3CiquxGwxtgH9SWo3iRy4',  'authorize_result': {'enterprise_id': None, 'team_id': 'T02NRMZN8NS', 'bot_user_id': 'U040J5JEFSB', 'bot_id': 'B040S4K565C', 'bot_token': 'xoxb-2773747756774-4018188491895-R1b3CiquxGwxtgH9SWo3iRy4', 'user_id': 'U02NVERT65B', 'user_token': None}, 'bot_id': 'B040S4K565C', 'bot_user_id': 'U040J5JEFSB', 'bot_token': 'xoxb-2773747756774-4018188491895-R1b3CiquxGwxtgH9SWo3iRy4',}


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr


jstr = convert_obj(ob)

text_file = open("data.json", "w")

text_file.write(jstr)
# print(text_file.read())

text_file.close()
