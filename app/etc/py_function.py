from datetime import datetime



time_str = '10:16:00 AM'

time_obj = datetime.strptime(time_str, '%I:%M:%S %p')

spend = datetime.now() - time_obj

print(spend)

