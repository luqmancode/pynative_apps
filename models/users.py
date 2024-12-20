from models.sqlite_sql import Database, DATABASE


def list_all_users():
    with Database(DATABASE) as db:
        query = ("SELECT id, username, email FROM users;")
        cur_users = db.execute(query)
        return cur_users.fetchall()


def user_list(id_: str):
    with Database(DATABASE) as db:
        query = ("SELECT username, email, full_name FROM users WHERE "
                 "id=:id or username=:id;")
        params = (id_,)
        cur_user = db.execute(query, params)
        return cur_user.fetchone()


def create_single_user(user):
    with Database(DATABASE) as db:
        query = ("INSERT INTO users(username, email, full_name, password) "
                 "VALUES(:username, :email, :full_name, :password)")
        params = (user.get('username'),
                  user.get('email'),
                  user.get('full_name'),
                  user.get('password'))
        db.execute(query, params)  # returns []


def delete_user(id_: str):
    with Database(DATABASE) as db:
        query = ("DELETE FROM users WHERE id=:id_;")
        params = (id_)
        db.execute(query, params) #  returns []
