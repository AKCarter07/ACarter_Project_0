from models.user import User
from models.account import Account
import psycopg
from exception.invalid_parameter import InvalidParamError


class AccountDao:

    def get_account(self, account_id, user_id):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_0.accounts WHERE accounts.user_id = '{user_id}' AND "
                            f"accounts.account_number = '{account_id}'")
                for line in cur:
                    account = Account(line[2], line[3], line[4])
                    return account

    def get_user_accounts(self, user_object):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_0.accounts WHERE accounts.user_id = '{user_object.get_idn()}'")
                user_object.set_accounts(cur)
                return user_object

    def edit_account(self, account_id, user_id, command, dollars, cents):
        with psycopg.connect(host="localhost", port="5432",
                             dbname="postgres", user="postgres", password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_0.accounts WHERE accounts.user_id = '{user_id}' AND "
                            f"accounts.account_number = '{account_id}'")
                for line in cur:
                    account = Account(line[2], line[3], line[4])
                    if command == 'withdraw':
                        account.withdraw(dollars, cents)
                    elif command == 'deposit':
                        account.deposit(dollars, cents)
                    else:
                        raise InvalidParamError(f"{command} is not a valid command.")
                    cur.execute(f"UPDATE project_0.accounts SET dollars = {account.get_dollars()}"
                                f", cents = {account.get_cents()} WHERE user_id = '{user_id}'"
                                f" AND account_number = '{account_id}';")
                    conn.commit()
                    return account

    def create_account(self, user_id, account_id, dollars, cents):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO project_0.accounts (user_id, account_number, dollars, cents)"
                            f"VALUES ('{user_id}', '{account_id}', {dollars}, {cents});")
                conn.commit()
        return f"Account {account_id} created with a starting balance of ${dollars}." \
               f"{'0' if cents < 10 else ''}{cents}"

    def delete_account(self, user_id, account_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="pass") as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM project_0.accounts WHERE user_id ='{user_id}' AND "
                            f"account_number = '{account_id}';")
                conn.commit()
        return f"Account {account_id} has been deleted."
