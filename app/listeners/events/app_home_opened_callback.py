from app.blocks.app_home_tab import app_home_tab
from app.blocks.home.not_completed_task_item import not_completed_task_item
# from app.gql.graph_ql_service import GraphQLService
# from app.gql.task_query import get_all_task


def app_home_opened_callback(client, event, logger):
    try:
        client.views_publish(
            user_id=event["user"],
            view=app_home_tab(blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Soft Bot Home*"
                    }
                },
            ])
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


def _create_app_blocks():
    blocks = not_completed_task_item(title="Title", description="description")
    blocks = blocks + \
        not_completed_task_item(title="Title 2", description="description 2")

    return blocks
