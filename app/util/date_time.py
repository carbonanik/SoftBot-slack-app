from datetime import datetime
from time import time


def now_date_str():
    d = datetime.now()
    return d.strftime("%Y-%m-%d")

def now_time_str():
    d = datetime.now()
    return d.strftime("%I:%M %p")

# def date_str(date_obj):
#     return date_obj.strftime("%Y-%m-%d")

# def time_str(time_obj):
#     return time_obj.strftime("%I:%M %p")