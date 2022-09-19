from curses import raw
from datetime import datetime
from slack_bolt import Ack
from logging import Logger
from slack_sdk import WebClient
# import gspread
from service_account import wks

from app.blocks.you_are_out_message import you_are_out
from app.util.date_time import now_date_str, now_time_str


def out_command(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()
       
        user_id = body['user_id']

        # sa = gspread.service_account()
        # sh = sa.open("Attendance Sheet")
        # wks = sh.worksheet("Current")

        data = wks.get_all_values()

        for i in range(len(data)):
            if data[i][0] == now_date_str() and data[i][2] == user_id and data[i][5] == '':

                wks.update(f'F{i+1}', now_time_str(), raw=False)

                time_out = datetime.strptime(data[i][4], '%I:%M %p')
                difference = datetime.now() - time_out
                hours, remainder = divmod(difference.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                total_hour = f'{hours}h {minutes}m'

                wks.update(f'G{i+1}', total_hour, raw=False)
                
                client.chat_postMessage(
                    channel="#soft-bot",
                    blocks=you_are_out(
                        name=data[i][1], 
                        date=now_date_str(),
                        task=data[i][3], 
                        time=now_time_str(),
                        working= total_hour,
                    )
                )

    except Exception as e:
        logger.error(e)
