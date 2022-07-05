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

# users = cs.get_all_users()
# x = len(users)
# print(x)
#
# print(ud.get_all_users())
# print(cs.get_all_users())

user1 = User('user1', 1001)
user1.set_num_active_accounts(2)
user1.set_total_accounts(2)
user2 = User('user2', 1002)
user2.set_num_active_accounts(1)
user2.set_total_accounts(1)
users = [user1.to_dict(), user2.to_dict()]

print(users)







# user1 = user_dao.get_user(user_id)
# print(user_dao.add_user(User('user3', 1003)))
# user3 = cs.get_user(1003)
# print(cs.delete_user(user3))
