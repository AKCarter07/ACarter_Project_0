from service.customer_service import CustomerService
from service.account_service import AccountService
from models.user import User
import psycopg


cs = CustomerService()
acs = AccountService()
user_id = 1001

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
        print(user)




