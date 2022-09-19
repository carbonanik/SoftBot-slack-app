from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.gql.graph_ql_service import GraphQLService
from app.gql.user_query import insertUserMutationStr
from app.blocks.member_created_modal import member_created_modal
from app.blocks.member_creation_failed_modal import member_cration_failed_modal
from app.blocks.loading_modal import loading_modal


def join_form_madal_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    # client.views_open(
    #     trigger_id=body["trigger_id"],
    #     view=loading_modal()
    # )
    
    print("join submit event")

    user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]

    full_name = state["full_name"]["plain_text_input-action"]["value"]
    email = state["email"]["plain_text_input-action"]["value"]
    phone = state["phone"]["plain_text_input-action"]["value"]
    title = state["title"]["plain_text_input-action"]["value"]

    q, v = insertUserMutationStr(
        name=full_name,
        email=email,
        phone=phone,
        slackUserId=user_id,
        title=title
    )

    response = GraphQLService().preformQuery(query=q, variables=v)

    if response.get("errors") != None:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=member_cration_failed_modal()
        )
    elif response.get("data") != None:
        # user = response["data"]["insert_user_one"]
        client.views_open(
            trigger_id=body["trigger_id"],
            view=member_created_modal()
        )
