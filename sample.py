# class Db:
#
#     def __init__(self):
#         self.conn = None
#
#     def connect_to_database(self):
#         self.conn = 'db'
#
#     def execute_query(self, query, *arg, **kwargs):
#         print(f"query is {query}")
#         print(f"args are {arg}")
#         print(f"kwargs are {kwargs}")
#
#     def insert(self):
#         self.execute_query('select *', 'arg1', 'arg2', ka1='karg1')
#
#
# db = Db()
# db.insert()

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
# 30, ]
#
#
# def ss(n):
#     n = n - 1
#     return arr[n * 7:n * 7 + 7]


# print(ss(5))

from datetime import datetime, timedelta

# Sun - Mon - Tue - Wed - Thu - Fri - Sat

# td = datetime.date.today() - datetime.timedelta(days=41)
# f = "%A : %Y-%m-%d"
# print(td.strftime(f))
# print("-----------------")
#
#
# def get_the_week(given_day, week_offset=0):
#     this_week = []
#     week_order = [0, 1, 2, 3, 4, 5, 6]
#     day_of_week = given_day.weekday()
#
#     for i in week_order:
#         this_week.append(given_day - datetime.timedelta(days=day_of_week - i - week_offset * 7))
#     return this_week
#
#
# this_week_arr = get_the_week(datetime.date.today(), week_offset=239)
# for d in this_week_arr:
#     print(d.strftime(f))
#

time_str = "7:00 am"
time_obj = datetime.strptime(time_str, '%I:%M %p')

sch_time = time_obj - timedelta(minutes=15)

sch_time_str = sch_time.strftime("%I:%M %p")
print(sch_time_str)

# num = 3456
# third_digit = num // 10 % 10
# print(num // 1000 % 10)
