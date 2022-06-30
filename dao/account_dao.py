from models.user import User
from models.account import Account
import psycopg

class AccountDao:

    def get_account(self, account_id, user_id):
        pass

    def get_user_accounts(self, user_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_0.users WHERE users.user_id = '{user_id}'")
                user = User(cur[1], cur[2])
                user.set_num_accounts(user[3])
                user.set_status(cur[4])
                with conn.cursor() as cur2:
                    cur2.execute(f"SELECT * FROM project_0.users WHERE accounts.user_id = '{user_id}'")
                    user.set_accounts(cur2)
                print(user)
