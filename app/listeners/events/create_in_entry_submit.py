from datetime import datetime
from logging import Logger

from slack_bolt import Ack, BoltContext
from slack_sdk import WebClient

from app.blocks.response.you_are_in import you_are_in
from app.util.date_time import now_date_str, now_time_str
# from service_account import wks
from app.db.db import Database


def create_in_submit_event(context: BoltContext, ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]

    # print(client.channels_info)

    task_name = state["task_name"]["plain_text_input-action"]["value"]

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
    local_tz = user_info['tz']
    # us_eastern_tz = 'US/Eastern'

    db = Database()
    db.connect_to_database()
    separate_task(task_name)
    inserted_att = db.in_attendance_if_not_already(slack_user_id, name)
    print(inserted_att)

    separated_task = separate_task(task_name)
    project_task = make_project_dict(separated_task)

    if inserted_att:
        tuple_list = project_dict_to_tuple(inserted_att[0]['id'], project_task)
        r = db.insert_task_many(tuple_list)

    # build_row = [None] * 20
    # build_row.insert(name_col, name)
    # build_row.insert(slack_id_col, slack_user_id)
    # build_row.insert(working_on_col, task_name)
    #
    # wks.insert_row(build_row, index=2)
    # wks.update(f'{col_letter[loacl_date_col]}2', now_date_str(local_tz), raw=False)
    # wks.update(f'{col_letter[us_date_col]}2', now_date_str(us_eastern_tz), raw=False)
    # wks.update(f'{col_letter[in_local_time_col]}2', now_time_str(local_tz), raw=False)
    # wks.update(f'{col_letter[in_us_time_col]}2', now_time_str(us_eastern_tz), raw=False)

    client.chat_postMessage(
        channel="#attendance-beta",
        blocks=you_are_in(
            name=name,
            # date=now_date_str(local_tz),
            # task=task_name,
            time=now_time_str(local_tz),
            tasks=separate_task(task_name)
        )
    )


def separate_task(task_str: str, separator=','):
    return list(filter(None, [s.strip() for s in task_str.split(separator)]))


def make_project_dict(separated_val):
    dictionary = {}
    last_p = '-'
    for item in separated_val:
        if item.startswith('#'):
            last_p = item[1:]
        else:
            if dictionary.get(last_p):
                prev = dictionary[last_p]
                dictionary[last_p] = prev + [item]
            else:
                dictionary[last_p] = [item]
    print(dictionary)
    return dictionary


def project_dict_to_tuple(att_id, project_task):
    tuple_list = []
    for proj in project_task:
        for task in project_task[proj]:
            t = (att_id, task, proj if proj != '-' else None)
            tuple_list.append(t)
    return tuple_list
