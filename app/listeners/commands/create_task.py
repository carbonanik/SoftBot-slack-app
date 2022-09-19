from ast import Str
from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient
from datetime import date

from app.blocks.loading_modal import loading_modal
from app.blocks.did_not_joined_modal import did_not_joined_madal
from app.blocks.create_task_modal import create_task_modal

from app.gql.graph_ql_service import GraphQLService
from app.gql.user_query import getUserBySlackUserId


def create_task(ack: Ack, client: WebClient, body: dict, logger: Logger):

    d = date.today()
    
    full_date = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

    # print(type(d))
    # print(d)
    # dt = "2020-04-28"

    try:
        trigger_id = body["trigger_id"]

        view_open_response = client.views_open(
            trigger_id=trigger_id,
            view=loading_modal()
        )
        ack()

        user_id = body['user_id']

        q, v = getUserBySlackUserId(slackUserId=user_id)
        a_user = GraphQLService().preformQuery(query=q, variables=v)

        if a_user["data"]["user"] == []:
            client.views_update(
                view_id=view_open_response["view"]["id"],
                hash=view_open_response["view"]["hash"],
                view=did_not_joined_madal()
            )

        else:
            client.views_update(
                view_id=view_open_response["view"]["id"],
                hash=view_open_response["view"]["hash"],
                view=create_task_modal(full_date)
            )

    except Exception as e:
        logger.error(e)


# def _user_info_to_join_form_model(user_info):
#     name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
#     email = user_info["profile"]["email"]
#     phone = user_info["profile"]["phone"]
#     title = user_info["profile"]["title"]

#     return join_form_modal(
#         name=name,
#         email=email,
#         phone=phone,
#         title=title
#     )
