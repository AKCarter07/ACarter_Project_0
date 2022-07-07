from service.customer_service import CustomerService
from service.account_service import AccountService
from models.user import User
import psycopg
from models.account import Account
from dao.user_dao import UserDao
from dao.account_dao import AccountDao

ud = UserDao()
ad = AccountDao()
cs = CustomerService()
acs = AccountService()
user_id = 1001
account_id = 10010001


acs.get_accounts(1001)
print(acs.get_accounts(1001))
# users = cs.get_all_users()
# x = len(users)
# print(x)
#
# print(ud.get_all_users())
# print(cs.get_all_users())
