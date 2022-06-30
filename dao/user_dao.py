from models.user import User
import psycopg
import copy
from dao.account_dao import AccountDao


class UserDao:
    def __init__(self):
        self.__account_dao = AccountDao()

    def get_user(self, user_id):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_0.users WHERE users.user_id = '{user_id}'")
                for line in cur:
                    user = User(line[2], line[1])
                    user.set_num_accounts(line[3])
                    user.set_status(line[4])
                    self.__account_dao.get_user_accounts(user)
                    return user

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
                    self.__account_dao.get_user_accounts(user_id)
                    users.append(user_object)
            return users

    def add_user(self, user_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO project_0.users (user_id, username) VALUES "
                            f"({user_object.get_idn()}, '{user_object.get_username()}')")
                conn.commit()
        return f"User {user_object.get_username()} ({user_object.get_idn()}) has been " \
               f"added to the system."

    def edit_user(self, user_id, new_info_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE project_0.users SET username = '{new_info_object.get_username()}', "
                            f"num_accounts = {new_info_object.get_num_accounts()}, active_user = "
                            f"{new_info_object.get_status()} WHERE user_id = '{user_id}'")
                conn.commit()
        return f"User updated. {new_info_object}"

    def delete_user(self, user_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM project_0.accounts WHERE user_id = '{user_object.get_idn()}';"
                            f"DELETE FROM project_0.users WHERE user_id = '{user_object.get_idn()}';")
        return f"User account for {user_object.get_username()} has been deleted."

