from slack_bolt import Ack, BoltContext
from logging import Logger
from slack_sdk import WebClient


from app.blocks.response.team_are_on_break import team_are_on_break
from app.db.db import Database


def team_break_submit_event(context: BoltContext, ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    print("fun fun ")
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]
    break_pac = state['team_break_radio']['team_break_select']['selected_option']['value']

    break_type = {
        '1': "Electricity break ⚡",
        '2': "Launch break 🍲",
    }

    print(break_pac)
    print("break_pac")

    user_info = client.users_info(user=slack_user_id)["user"]
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]

    db = Database()
    db.connect_to_database()
    db.insert_team_break(break_type[break_pac])

    client.chat_postMessage(
        channel="#attendance-beta",
        blocks=team_are_on_break(break_type[break_pac])
    )
