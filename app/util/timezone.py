from datetime import datetime

from pytz import timezone

# for zone in all_timezones:
#     if zone.find('PDT') != -1:
#         print(zone)
time_format = '%d-%m-%Y %I:%M'
now = datetime.now().strftime(time_format)
print(now)

tz = ['US/Eastern', 'US/Central', 'Europe/London', 'Europe/Amsterdam', 'Asia/Dhaka', 'UTC', 'PST8PDT']

for zone in tz:
    dt = datetime.now(timezone(zone)).strftime(time_format)
    print(f'Date Time in {zone} is {dt}')