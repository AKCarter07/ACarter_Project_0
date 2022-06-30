from models.user import User
from exception.user_not_found import UserNotFound
import psycopg
import copy


class UserDao:

    def get_user(self, user_id):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_0.users WHERE users.user_id = '{user_id}'")
                for line in cur:
                    user = User(line[1], line[2])
                    user.set_num_accounts(line[3])
                    user.set_status(line[4])
                    with conn.cursor() as cur2:
                        cur2.execute(f"SELECT * FROM project_0.accounts WHERE accounts.user_id = '{user_id}'")
                        user.set_accounts(cur2)

    def get_all_users(self):
        users = []
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project_0.users")
                for user in cur:
                    user_id = user[1]
                    username = user[2]
                    user_object = User(username, user_id)
                    user_object.set_num_accounts(user[3])
                    with conn.cursor() as cur2:
                        cur2.execute(f"SELECT * FROM project_0.accounts WHERE accounts.user_id = '{user_id}'")
                        user.set_accounts(cur2)
                    users.append(user_object)
            return users

    def add_user(self, user_object):
        pass

    def edit_user(self, username, new_user_info_object):
        if username == new_user_info_object.username:
            pass
        else:
            pass
        return new_user_info_object

    def delete_user(self, username):

        return f"User account for {username} has been deleted."

