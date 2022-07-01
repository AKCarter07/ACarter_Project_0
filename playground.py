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

print(acs.get_accounts(1001))

print(acs.withdraw(1001, 10010001, 10, 0))
print(acs.deposit(1001, 10010001, 10, 5))

print(acs.add_account(1005, 100, 25))
# print(acs.delete_account(1001, 10010004))







# user1 = user_dao.get_user(user_id)
# print(user_dao.add_user(User('user3', 1003)))
# user3 = cs.get_user(1003)
# print(cs.delete_user(user3))
