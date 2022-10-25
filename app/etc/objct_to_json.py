import json


ob = {'ok': True, 'user': {'id': 'U02NVERT65B', 'team_id': 'T02NRMZN8NS', 'name': 'shkhnk', 'deleted': False, 'color': '9f69e7', 'real_name': 'Sheikh Anik', 'tz': 'Asia/Dhaka', 'tz_label': 'Bangladesh Standard Time', 'tz_offset': 21600, 'profile': {'title': 'App Developr', 'phone': '+8801766785027', 'skype': '', 'real_name': 'Sheikh Anik', 'real_name_normalized': 'Sheikh Anik', 'display_name': '', 'display_name_normalized': '', 'fields': None, 'status_text': 'Vacationing', 'status_emoji': ':palm_tree:', 'status_emoji_display_info': [], 'status_expiration': 0, 'avatar_hash': 'g6d7715adf3c', 'email': 'shkhnk@gmail.com', 'first_name': 'Sheikh', 'last_name': 'Anik', 'image_24': 'https://secure.gravatar.com/avatar/6d7715adf3cc3c15fc72c211036bbdf1.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-24.png', 'image_32': 'https://secure.gravatar.com/avatar/6d7715adf3cc3c15fc72c211036bbdf1.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-32.png', 'image_48': 'https://secure.gravatar.com/avatar/6d7715adf3cc3c15fc72c211036bbdf1.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-48.png', 'image_72': 'https://secure.gravatar.com/avatar/6d7715adf3cc3c15fc72c211036bbdf1.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-72.png', 'image_192': 'https://secure.gravatar.com/avatar/6d7715adf3cc3c15fc72c211036bbdf1.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-192.png', 'image_512': 'https://secure.gravatar.com/avatar/6d7715adf3cc3c15fc72c211036bbdf1.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-512.png', 'status_text_canonical': 'Vacationing', 'team': 'T02NRMZN8NS'}, 'is_admin': True, 'is_owner': True, 'is_primary_owner': True, 'is_restricted': False, 'is_ultra_restricted': False, 'is_bot': False, 'is_app_user': False, 'updated': 1662277038, 'is_email_confirmed': True, 'who_can_share_contact_card': 'EVERYONE'}}


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr

jstr = convert_obj(ob)


text_file = open("data.json", "w")

text_file.write(jstr)
# print(text_file.read())
 
text_file.close()