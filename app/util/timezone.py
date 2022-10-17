from pytz import timezone, all_timezones
from datetime import datetime

for zone in all_timezones:
    print(zone)
# time_format = '%d-%m-%Y %I:%M'
# now = datetime.now().strftime(time_format)
# print(now)

# tz = ['US/Eastern', 'US/Central', 'Europe/London', 'Europe/Amsterdam', 'Asia/Dhaka', 'UTC']

# for zone in tz:
#     dt = datetime.now(timezone(zone)).strftime(time_format)
#     print(f'Date Time in {zone} is {dt}')