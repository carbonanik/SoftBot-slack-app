from os import stat
from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient

from app.gql.graph_ql_service import GraphQLService
from app.gql.task_query import insert_task
from app.gql.user_query import getUserBySlackUserId
from app.blocks.task_created_modal import task_created_modal
from app.blocks.task_creation_failed_modal import task_cration_failed_modal
from app.blocks.loading_modal import loading_modal


def create_task_madal_submit_event(ack: Ack, body: dict, client: WebClient, view, logger: Logger):
    ack()

    slack_user_id = body["user"]["id"]
    state = body["view"]["state"]["values"]
    # print(state)

    task_name = state["task_name"]["plain_text_input-action"]["value"]
    description = state["description"]["plain_text_input-action"]["value"]
    deadline = state["deadline"]["datepicker-action"]["selected_date"]

    q, v = getUserBySlackUserId(slackUserId=slack_user_id)
    a_user_response = GraphQLService().preformQuery(query=q, variables=v)
    a_user = a_user_response["data"]["user"][0]

    q2, v2 = insert_task(
        title=task_name,
        description=description,
        dueDate=deadline,
        userId=a_user["id"]
    )

    response = GraphQLService().preformQuery(query=q2, variables=v2)

    if response.get("errors") != None:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=task_cration_failed_modal()
        )
    elif response.get("data") != None:
        # user = response["data"]["insert_task_one"]
        client.views_open(
            trigger_id=body["trigger_id"],
            view=task_created_modal()
        )


# {
#     'task_name': {
#         'plain_text_input-action': {
#             'type': 'plain_text_input',
#             'value': 'New Task'
#         }
#     },
#     'description': {
#         'plain_text_input-action': {
#             'type': 'plain_text_input',
#             'value': 'Task Des'
#         }
#     },
#     'deadline': {
#         'datepicker-action': {
#             'type': 'datepicker',
#             'selected_date': '1990-04-28'
#         }
#     }
# }
