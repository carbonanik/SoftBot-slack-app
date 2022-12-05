import os

import psycopg2
import sys
from functools import wraps

from dotenv import load_dotenv


# DB_NAME = "softbot"
# DB_USER = "postgres"
# DB_PASS = "password"
# DB_HOST = "143.244.169.231"
# DB_PORT = "5432"

# load_dotenv()
# DB_NAME = os.getenv('DB_NAME', "softbot")
# DB_USER = os.getenv('DB_USER', "postgres")
# DB_PASS = os.getenv('DB_PASS', "password")
# DB_HOST = os.getenv('DB_HOST', "143.244.169.231")
# DB_PORT = os.getenv('DB_PORT', "5432")

# postgres://postgres:password@143.244.169.231:5432/explore_prisma

def decorator_function(original_function):
    @wraps(original_function)
    def wrapper(self, *args, **kwargs):
        print(args)

        def execute(sql):
            dict_array = []
            try:
                cur = self.conn.cursor()
                cur.execute(sql, args)

                try:
                    rows = cur.fetchall()
                    # print(cur.description)
                    for row in rows:
                        dict_item = {}
                        for ind, cel in enumerate(row):
                            dict_item[cur.description[ind].name] = cel
                        dict_array.append(dict_item)

                except Exception as e:  # work on python 3.x
                    print(e.with_traceback(sys.exc_info()[2]))

                self.conn.commit()

            except Exception as e:  # work on python 3.x
                print(e.with_traceback(sys.exc_info()[2]))

            return dict_array

        return original_function(self, execute, *args, **kwargs)

    return wrapper


class Database:
    def __init__(self):
        self.conn = None
        # self.connect_to_database()

    def connect_to_database(self):
        load_dotenv()
        DB_NAME = os.getenv('DB_NAME', "softbot")
        DB_USER = os.getenv('DB_USER', "postgres")
        DB_PASS = os.getenv('DB_PASS', "password")
        DB_HOST = os.getenv('DB_HOST', "143.244.169.231")
        DB_PORT = os.getenv('DB_PORT', "5432")
        try:
            self.conn = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT
            )

            print("Database connected successfully")

        except:
            print("Database not connected successfully")

    def execute_query(self, q, *arg):
        cur = self.conn.cursor()
        cur.execute(q, *arg)
        self.conn.commit()

    @decorator_function
    def create_tables(self, execute):
        return execute(open("app/db/database.sql", "r").read())

    # ----------------------------- attendance
    @decorator_function
    def in_attendance_if_not_already(self, execute, slack_id, name):
        return execute('SELECT * FROM in_attendance_if_not_already(%s, %s)')

    @decorator_function
    def insert_attendance(self, execute, participant_id):
        return execute(
            "INSERT INTO attendance (in_time, on_break, participant_id) VALUES (NOW(), false, %s) RETURNING *;")

    @decorator_function
    def get_attendance_by_participant_id_where_out_time_null(self, execute, participant_id):
        return execute("SELECT * FROM attendance WHERE participant_id=%s AND out_time IS NULL;")

    @decorator_function
    def get_last_attendance_where_not_out(self, execute, participant_id):
        return execute("""
            SELECT * FROM attendance 
            WHERE participant_id=%s AND out_time IS NULL 
            ORDER BY in_time DESC LIMIT 1;
        """)

    @decorator_function
    def update_attendance_out_time_by_id(self, execute, attendance_id):
        return execute("UPDATE attendance SET out_time=NOW() WHERE id=%s RETURNING *;")

    @decorator_function
    def today_attendance(self, execute):
        return execute("SELECT * FROM attendance WHERE DATE(in_time) = DATE(NOW());")

    @decorator_function
    def all_attendance_of_today_with_joined_tasks(self, execute):
        return execute(open("app/db/all_attendance_of_today_with_joined_tasks.sql", "r").read())  # app/db/

    # out command
    @decorator_function
    def update_out_time(self, execute, slack_id):
        return execute("SELECT * FROM update_out_time(%s);")

    # @decorator_function
    # def get_last_in_of_every_user(self, execute, date):
    #     return execute(open("app/db/get_last_in_of_every_user.sql", "r").read())

    @decorator_function
    def get_last_attendance_of_day(self, execute, day):
        return execute(open("app/db/get_last_attendance_of_day.sql", "r").read())

    @decorator_function
    def get_tasks_by_attendance_ids(self, execute, attendance_ids):
        return execute(open("app/db/get_tasks_by_attendance_ids.sql", "r").read())

    # --------------------------------------------------------------
    # individual break command
    @decorator_function
    def insert_break_if_possible(self, execute, slack_id, break_length):
        return execute("SELECT * FROM inset_break_if_possible(%s, %s);")

    @decorator_function
    def insert_break(self, execute, length, attendance_id):
        return execute("""
            INSERT INTO break_ (break_length, started, attendance_id) 
            VALUES (%s, NOW(), %s);
        """)

    @decorator_function
    def get_not_ended_break(self, execute, attendance_id):
        return execute("""
            SELECT * FROM break_ 
            WHERE attendance_id=%s AND NOT (
                ended IS NOT NULL OR NOW() > started + break_length
            );
        """)

    @decorator_function
    def update_ended_in_break(self, execute, break_id):
        return execute('UPDATE break_ SET ended=now() WHERE id=%s RETURNING *;')

    # individual break ended command
    @decorator_function
    def update_break_ended(self, execute, slack_id):
        return execute(open("app/db/update_break_ended.sql", "r").read())

    # --------------------------------------------------------------
    @decorator_function
    def insert_team_break(self, execute, reason):
        return execute(open("app/db/insert_team_break.sql", "r").read())

    @decorator_function
    def update_team_break_ended(self, execute):
        return execute(open("app/db/update_team_break_ended.sql", "r").read())

    # -------------------------------------------------------------
    @decorator_function
    def get_all_participant(self, execute):
        return execute(open("app/db/get_all_participant.sql", "r").read())

    # ------------------------ task

    @decorator_function
    def insert_task(self, execute, title, participant_id, project_id):
        return execute(
            "insert into task (created_at, updated_at, title, participant_id, project_id)"
            " values (now(), now(), %s, %s, %s) RETURNING * ;"
        )

    @decorator_function
    def get_task_by_id(self, execute, task_id):
        return execute("SELECT * FROM task WHERE id=%s;")

    @decorator_function
    def get_tasks_project_id(self, execute, project_id):
        return execute("SELECT * FROM task WHERE project_id=%s;")

    @decorator_function
    def get_tasks_by_ids(self, execute, task_ids):
        return execute("SELECT * FROM task  WHERE id IN %s;")

    @decorator_function
    def get_task_uncompleted_filtered(self, execute, participant_id, project_id):
        return execute("SELECT * FROM task WHERE ended_at IS NULL AND participant_id=%s AND project_id=%s;")

    @decorator_function
    def task_update_started_at(self, execute, task_id):
        return execute("UPDATE task SET started_at=NOW(), status=1 WHERE id=%s;")

    @decorator_function
    def task_update_ended_at(self, execute, task_id):
        return execute("UPDATE task SET ended_at=NOW(), status=2 WHERE id=%s;")

    @decorator_function
    def get_in_progress_task_by_participant_id(self, execute, participant_id):
        return execute("SELECT * FROM task WHERE status=1 AND participant_id=%s;")

    def insert_task_many2(self, execute, tasks):
        return execute("")

    def insert_task_many(self, tasks):
        cur = self.conn.cursor()

        data_text = ','.join(cur.mogrify('(%s,%s,%s)', row).decode('utf-8') for row in tasks)

        sql_txt = """INSERT INTO task (attendance_id, title, project) VALUES {0} RETURNING *""".format(data_text)

        cur.execute(sql_txt)
        num_row = cur.rowcount
        rows = cur.fetchall()
        self.conn.commit()
        print(rows)
        print(f'number of rows inserted = {num_row}')

        dict_array = []
        for row in rows:
            dict_item = {}
            for ind, cel in enumerate(row):
                dict_item[cur.description[ind].name] = cel
            dict_array.append(dict_item)

        return dict_array
        # if self.conn:
        #     cur.close()
        #     conn.close()

    # ----------------------------- participant
    @decorator_function
    def insert_participant(self, execute, slack_id, name, email, phone, designation):
        return execute(open("app/db/insert_participant.sql", "r").read())

    @decorator_function
    def get_participant_by_slack_id(self, execute, slack_id):
        return execute(open("app/db/get_participant_by_slack_id.sql", "r").read())

    # ----------------------------- project

    @decorator_function
    def insert_project(self, execute, title, description, participant_id):
        return execute('''
            insert into project (started_at, title, description, participant_id)
            values (now(), %s, %s, %s) returning *;
        ''')

    @decorator_function
    def get_projects(self, execute):
        return execute("SELECT * FROM project;")

    @decorator_function
    def get_project_by_id(self, execute, project_id):
        return execute("SELECT * FROM project WHERE id=%s;")

    @decorator_function
    def get_projects_by_ids(self, execute, project_ids):
        return execute('SELECT * FROM project WHERE id IN %s;')

    @decorator_function
    def get_project_by_task_id(self, execute, task_id):
        return execute("SELECT project.* FROM task INNER JOIN project ON task.project_id=project.id WHERE task.id=%s;")

    @decorator_function
    def get_project_by_task_ids(self, execute, task_ids):
        return execute('''
            SELECT DISTINCT project.* FROM task 
            INNER JOIN project ON task.project_id=project.id WHERE task.id IN %s;
        ''')

    # --------------------------- review
    @decorator_function
    def insert_review(self, execute, description, task_id, participant_id):
        return execute("INSERT INTO review (description, task_id, participant_id) VALUES (%s, %s, %s);")

    # --------------------------- blocker
    @decorator_function
    def insert_blocker(self, execute, description, project_id, participant_id):
        return execute("INSERT INTO blocker (description, project_id, participant_id) VALUES (%s, %s, %s);")

    @decorator_function
    def get_blockers(self, execute):
        return execute('SELECT * FROM blocker;')

    # ---------------------------- attendance_to_task
    @decorator_function
    def insert_relation_attendance_to_task(self, execute, attendance_id, task_id):
        return execute('INSERT INTO "_attendanceTotask" ("A", "B") VALUES (%s, %s);')


# db = Database()
# db.connect_to_database()
# print(db.get_tasks_by_ids((30, 31)))
# db.get_projects_by_ids()
