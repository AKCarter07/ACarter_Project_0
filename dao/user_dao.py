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
                    print(line)
                    user = User(line[2], line[1])
                    user.set_num_active_accounts(line[4])
                    user.set_total_accounts(line[3])
                    user.set_status(line[5])
                    self.__account_dao.get_user_accounts(user)
                    print(user)
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
                    user_object.set_num_active_accounts(user[4])
                    user_object.set_total_accounts(user[3])
                    user_object.set_status(user[5])
                    self.__account_dao.get_user_accounts(user_object)
                    users.append(user_object)
            return users

    def add_user(self, user_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO project_0.users (user_id, username) VALUES "
                            f"({user_object.get_idn()}, '{user_object.get_username()}');"
                            f"INSERT INTO project_0.used_idns (user_id) VALUES ('{user_object.get_idn()}');")
                conn.commit()
        return f"User {user_object.get_username()} ({user_object.get_idn()}) has been " \
               f"added to the system."

    def edit_user(self, user_id, new_info_object):
        previous_info = self.get_user(user_id)
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE project_0.users SET username = '{new_info_object.get_username()}', "
                            f"num_accounts = {new_info_object.get_num_accounts()}, num_active_accounts = "
                            f"{new_info_object.get_num_active_accounts()}, active_user = "
                            f"{new_info_object.get_status()} WHERE user_id = '{user_id}'")
                conn.commit()
                edited_user = self.get_user(user_id)
        return f"User has been updated: {edited_user}"

    def delete_user(self, user_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM project_0.accounts WHERE user_id = '{user_object.get_idn()}';"
                            f"DELETE FROM project_0.users WHERE user_id = '{user_object.get_idn()}';")
        return f"User account for {user_object.get_username()} has been deleted."

    def number_idns(self):
        idns = []
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project_0.used_idns;")
                for line in cur:
                    idns.append(line)
                return len(idns)
