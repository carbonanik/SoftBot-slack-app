from curses import raw
from datetime import datetime
from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient
# import gspread
from service_account import wks

from app.blocks.you_are_out_message import you_are_out
from app.util.date_time import now_date_str, now_time_str
from app.util.const import date_col, name_col, slack_id_col, working_on_col, in_time_col, out_time_col, total_hour_col


def out_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()
       
        user_id = body['user_id']

        # sa = gspread.service_account()
        # sh = sa.open("Attendance Sheet")
        # wks = sh.worksheet("Current")

        data = wks.get_all_values()

        for i in range(len(data)):
            if data[i][date_col] == now_date_str() and data[i][slack_id_col] == user_id and data[i][out_time_col] == '':

                wks.update(f'F{i+1}', now_time_str(), raw=False)

                time_in = datetime.strptime(data[i][in_time_col], '%I:%M %p')
                difference = datetime.now() - time_in
                hours, remainder = divmod(difference.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                total_hour = f'{hours}h {minutes}m'

                wks.update(f'G{i+1}', total_hour, raw=False)
                
                client.chat_postMessage(
                    channel="#soft-bot",
                    blocks=you_are_out(
                        name=data[i][name_col], 
                        date=now_date_str(),
                        task=data[i][working_on_col], 
                        time=now_time_str(),
                        working= total_hour,
                    )
                )

    except Exception as e:
        logger.error(e)
