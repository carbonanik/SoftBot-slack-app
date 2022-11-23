# from ast import Str


# ----------------------------------------
#
# def insertAttendance(task: Str, slackUserId: Str, userId: int):
#     query = """
#     mutation insertAttendance($inTime: timestamp, $slackUserId: String, $task: String, $userId: Int) {
#         insert_attendance_one(object: {inTime: $inTime, slackUserId: $slackUserId, task: $task, userId: $userId}) {
#             id
#             inTime
#             outTime
#             slackUserId
#             task
#             userId
#         }
#     }
#     """
#     variables = {
#         "inTime": "now()",
#         "slackUserId": slackUserId,
#         "task": task,
#         "userId": userId
#     }
#     return query, variables
#
#
# def updateAttendanceOutTime():
#     pass
#
#
# """
# query getLastAttendance {
#   attendance(limit: 1, order_by: {inTime: desc}) {
#     id
#     inTime
#     outTime
#     slackUserId
#     task
#     userId
#   }
# }
# """
