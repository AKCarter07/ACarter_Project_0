from service.customer_service import CustomerService
from service.account_service import AccountService
from models.user import User
import psycopg
from models.account import Account
from dao.user_dao import UserDao
from dao.account_dao import AccountDao



cs = CustomerService()
acs = AccountService()
user_id = 1001
account_id = 10010001
user_dao = UserDao()
account_dao = AccountDao()
# user1 = user_dao.get_user(user_id)
# print(user1)
# print(account_dao.edit_account(account_id, user_id, 'deposit', 20, 20))
# print(account_dao.edit_account(account_id, user_id, 'withdraw', 20, 10))
# print(account_dao.get_user_accounts(user1))
#
# user3 = User('user3', 1003)
# print(user_dao.add_user(User('user3', 1003)))
#
# print(account_dao.create_account('1003', '10030003', 25, 25))
#
# print(user_dao.delete_user(user3))
# new4 = user_dao.get_user(1004)
# new4.set_num_accounts(1)
#
# print(user_dao.edit_user(1004, new4))

# print(acs.get_accounts(1001))
print(cs.get_all_users())