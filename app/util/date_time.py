from datetime import datetime
from time import time
from pytz import timezone, all_timezones, utc
import re
from datetime import timedelta


def now_date_str(tz):
    d = datetime.now(timezone(tz))
    return d.strftime("%Y-%m-%d")


def now_time_str(tz):
    d = datetime.now(timezone(tz))
    return d.strftime("%I:%M %p")


def calculate_total_hour(in_time, tz):
    time_in = time_str_to_time(in_time)
    difference = time_str_to_time(now_time_str(tz)) - time_in
    return difference


def time_str_to_time(t):
    return datetime.strptime(t, '%I:%M %p')


def time_delta_to_str(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_str = f'{hours}h {minutes}m'
    return time_str


regex = re.compile(r'((?P<hours>\d+?)h) ((?P<minutes>\d+?)m)')


def parse_time(time_str):
    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for name, param in parts.items():
        if param:
            time_params[name] = int(param)
    return timedelta(**time_params)

# ================================= time digfference ==========================================
# time = '4:00 PM'

# dhaka = timezone('Asia/Dhaka')

# time_obj = datetime.strptime(time, '%I:%M %p')#.astimezone(timezone('Asia/Dhaka'))
# time_obj = dhaka.localize(time_obj)

# now_time = datetime.now(dhaka)

# difference = now_time - time_obj
# hours, remainder = divmod(difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)
# total_hour = f'{hours}h {minutes}m'

# print(time_obj)
# print(now_time)
# print(total_hour)
# ============================================================================+++++++++++
