import os

import psycopg2
from dotenv import load_dotenv


class Database:

    def __init__(self):
        load_dotenv()
        self.conn = self.connect_to_database(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

    @staticmethod
    def connect_to_database(database, user, password, host, port):
        try:
            conn = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            print('Connected to database')
            return conn
        except Exception as e:
            print(e)
            raise e

    @staticmethod
    def with_connection(func):
        def connection(self, *args, **kwargs):
            cur = self.conn.cursor()
            try:
                func(self, cur, *args, **kwargs)
            except Exception as e:
                print(e)
                self.conn.rollback()
            else:
                self.conn.commit()
            return self.fetch_as_dict(cur)

        return connection

    # convert row to dictionary with the associated colum name
    @staticmethod
    def fetch_as_dict(cur):
        dict_array = []
        try:
            rows = cur.fetchall()

            for row in rows:
                dict_item = {}

                for ind, cel in enumerate(row):
                    dict_item[cur.description[ind].name] = cel
                dict_array.append(dict_item)

        except Exception as e:
            print(e)
        finally:
            cur.close()
        return dict_array

    # @with_connection
    # def insert_project(self, cur, participant_id):
    #     cur.execute(
    #         '''
    #             SELECT * FROM project WHERE participant_id=%s;
    #         ''',
    #         (participant_id,)
    #     )
    #
    #

