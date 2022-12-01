from app.db.database import Database

db = Database()


def pass_db(func):
    def wrap(*args, **kwargs):
        return func(db, *args, **kwargs)
    return wrap


@pass_db
@db.with_connection
def insert_project(self, cur, participant_id):
    cur.execute(
        '''
            SELECT * FROM project WHERE participant_id=%s;
        ''',
        (participant_id,)
    )


v = insert_project(participant_id=7)
print(v)

# def insert_project_w(participant_id):
#     return insert_project(self=db, participant_id=7)
