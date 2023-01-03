from logging import Logger
from typing import List

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.block.block import markdown_text
from app.db.db import Database
from app.features.in_feature.block_message.select_projects import select_projects


def on_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        slack_id = body["event"]["user"]
        channel_id: str = channel_id_if_dm(context)

        db = init_db()

        projects = validate_all_and_get_projects(
            db=db,
            client=client,
            slack_id=slack_id,
            channel_id=channel_id
        )

        projects_array_of_dict = projects_array_of_dict_from_row(projects)

        client.chat_postMessage(
            channel=channel_id,
            blocks=select_projects(
                projects_array_of_dict=projects_array_of_dict
            )
        )

    except Exception as e:
        logger.error(e)


def init_db():
    # init database
    db = Database()
    db.connect_to_database()
    return db


def channel_id_if_dm(context):
    channel_id: str = context['channel_id']

    is_dm = channel_id.startswith("D")
    if not is_dm:
        raise Exception('Not a dm')
    return channel_id


def data_is_empty(data_list: List,
                  notice: str,
                  channel_id: str,
                  client: WebClient,
                  error_message: str = 'Data Empty'):
    if not data_list:
        client.chat_postMessage(
            channel=channel_id,
            blocks=[markdown_text(
                markdown=notice
            )]
        )
        raise Exception(error_message)


def validate_all_and_get_projects(db: Database, client: WebClient, slack_id, channel_id):
    # check participant existence
    participant = db.get_participant_by_slack_id(slack_id)
    data_is_empty(
        data_list=participant,
        notice='To participate in attendance write `start`',
        channel_id=channel_id,
        client=client,
    )

    # check project not empty
    projects = db.get_projects()
    data_is_empty(
        data_list=projects,
        notice='No Project have been created, To create project `add project`',
        channel_id=channel_id,
        client=client,
    )
    return projects


def projects_array_of_dict_from_row(projects):
    return list(map(
        lambda p: {
            "text": f'*{p["title"]}*',
            "value": str(p["id"])},
        projects
    ))
