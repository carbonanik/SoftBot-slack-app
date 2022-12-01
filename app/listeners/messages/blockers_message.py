from logging import Logger

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from app.blocks.response.project_blockers_blocks import project_blockers_blocks
from app.db.db import Database


def blockers_message(context: BoltContext, client: WebClient, body: dict, say: Say, logger: Logger):
    try:
        slack_id = body["event"]["user"]

        channel_id: str = context['channel_id']
        is_dm = channel_id.startswith("D")

        if not is_dm:
            return

        db = Database()
        db.connect_to_database()
        blockers = db.get_blockers()

        project_ids = tuple(set(map(lambda b: b['project_id'], blockers)))

        projects = db.get_projects_by_ids(project_ids)

        # project_blockers = list(map(
        #     lambda project: {
        #         'project': project['title'],
        #         'blocker': [
        #             blocker['description'] for blocker in blockers
        #             if blocker['project_id'] == project['id']
        #         ]
        #     }, projects
        # ))

        project_blockers = [{
            'project': project['title'],
            'blocker': [
                blocker['description'] for blocker in blockers
                if blocker['project_id'] == project['id']
            ]
        } for project in projects]

        client.chat_postMessage(
            channel=context['channel_id'],
            blocks=project_blockers_blocks(
                project_blockers=project_blockers
            )
        )

    except Exception as e:
        logger.error(e)
