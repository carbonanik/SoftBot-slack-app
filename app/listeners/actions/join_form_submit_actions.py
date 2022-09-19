from cgitb import reset
from logging import Logger

from slack_bolt import Ack, Say
from slack_sdk import WebClient

from app.gql.graph_ql_service import GraphQLService
from app.gql.user_query import insertUserMutationStr


def join_form_submit(ack: Ack, client: WebClient, body: dict, say: Say, logger: Logger):

    ack()

    user_id = body["user"]["id"]
    state = body["state"]["values"]

    full_name = state["full_name"]["plain_text_input-action"]["value"]
    email = state["email"]["plain_text_input-action"]["value"]
    phone = state["phone"]["plain_text_input-action"]["value"]
    title = state["title"]["plain_text_input-action"]["value"]

    print({
        "Full name": full_name,
        "Email": email,
        "Phone": phone,
        "Title": title
    })

    # q, v = insertUserMutationStr(
    #     name=full_name,
    #     email=email,
    #     phone=phone,
    #     slackUserId=user_id,
    #     title=title
    # )

    # response = GraphQLService().preformQuery(query=q, variables=v)

    # if response["errors"] != None:

    # client.views_update(
    #     # Pass the view_id
    #     view_id=body["view"]["id"],
    #     # String that represents view state to protect against race conditions
    #     hash=body["view"]["hash"],
    #     # View payload with updated blocks
    #     view={
    #         "type": "modal",
    #         # View identifier
    #         "callback_id": "view_1",
    #         "title": {"type": "plain_text", "text": "Updated modal"},
    #         "blocks": [
    #             {
    #                 "type": "section",
    #                 "text": {"type": "plain_text", "text": "You updated the modal!"}
    #             },
    #             {
    #                 "type": "image",
    #                 "image_url": "https://media.giphy.com/media/SVZGEcYt7brkFUyU90/giphy.gif",
    #                 "alt_text": "Yay! The modal was updated"
    #             }
    #         ]
    #     }
    # )

    # say("Request approved 👍")


# User created

# {'Full name': 'Sheikh Anik', 'Email': 'shkhnk@gmail.com', 'Phone': '+8801766785027', 'Title': 'App Developr'}
# DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): fit-hagfish-80.hasura.app:443
# DEBUG:urllib3.connectionpool:https://fit-hagfish-80.hasura.app:443 "POST /v1/graphql HTTP/1.1" 200 None
# {'data': {'insert_user_one': {'email': 'shkhnk@gmail.com', 'id': 2, 'name': 'Sheikh Anik', 'phone': '+8801766785027', 'slackUserId': 'U02NVERT65B', 'title': 'App Developr'}}}

# Failed
# {'errors': [{'extensions': {'code': 'constraint-violation', 'path': '$.selectionSet.insert_user_one.args.object'}, 'message': 'Uniqueness violation. duplicate key value violates unique constraint "user_slackUserId_key"'}]}
