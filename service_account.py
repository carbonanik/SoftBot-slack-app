import json
import gspread
import os

file = os.environ.get("SERVICE_ACCOUNT")
jsons = json.loads(file)

# print(jsons['type'])
sa = gspread.service_account_from_dict(jsons)
sh = sa.open("Attendance Sheet")
wks = sh.worksheet("Current")

# print("Row: ", wks.row_count)
# print("Col: ", wks.col_count)

# print(wks.acell('A1').value)
# print(wks.cell(col=3, row=6).value)
# print(wks.get('B4:D16')) // get list of list 
# wks.update('A3', 'Device No.')
# wks.update('B4:C5', [['Dev 1', 'Loc 1'], ['Dev 2', 'Loc 2']])
# wks.update('C3', '=UPPER(C6)', raw = False)
# wks.insert_row([32, 'MCP-2', 'Fire Control Room', 'OK'], index=4)