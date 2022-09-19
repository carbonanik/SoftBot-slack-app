from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.blocks.loading_modal import loading_modal
from app.blocks.join_form_modal import join_form_modal
from app.blocks.already_joined_modal import already_joined_modal

from app.gql.graph_ql_service import GraphQLService
from app.gql.user_query import getUserBySlackUserId


def join_attendance(ack: Ack, client: WebClient, body: dict, logger: Logger):

    try:
        trigger_id = body["trigger_id"]

        view_open_response = client.views_open(
            trigger_id=trigger_id,
            view=loading_modal()
        )
        ack()

        user_id = body['user_id']
        user_info = client.users_info(user=user_id)["user"]

        q, v = getUserBySlackUserId(slackUserId=user_id)
        a_user = GraphQLService().preformQuery(query=q, variables=v)

        if a_user["data"]["user"] == []:
            client.views_update(
                view_id=view_open_response["view"]["id"],
                hash=view_open_response["view"]["hash"],
                view=_user_info_to_join_form_model(user_info=user_info)
            )

        else:
            client.views_update(
                view_id=view_open_response["view"]["id"],
                hash=view_open_response["view"]["hash"],
                view=already_joined_modal()
            )

    except Exception as e:
        logger.error(e)


def _user_info_to_join_form_model(user_info):
    name = user_info["real_name"] if user_info["real_name"] else user_info["name"]
    email = user_info["profile"]["email"]
    phone = user_info["profile"]["phone"]
    title = user_info["profile"]["title"]

    return join_form_modal(
        name=name,
        email=email,
        phone=phone,
        title=title
    )
