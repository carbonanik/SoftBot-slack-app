from cgitb import reset
from logging import Logger

from slack_bolt import Ack, Say
from slack_sdk import WebClient

from app.gql.graph_ql_service import GraphQLService
from app.gql.user_query import insertUserMutationStr


def giga_break_action(ack: Ack, client: WebClient, body: dict, say: Say, logger: Logger):

    ack()

    user_id = body["user"]["id"]
    state = body["state"]["values"]

    print(state)