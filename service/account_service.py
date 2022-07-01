from dao.user_dao import UserDao
from dao.account_dao import AccountDao
from exception.invalid_parameter import InvalidParamError


class AccountService:
    def __init__(self):
        self.__user_dao = UserDao()
        self.__account_dao = AccountDao()

    def get_accounts(self, user_id):
        user_obj = self.__user_dao.get_user(user_id)
        return user_obj

    def withdraw(self, username, account, amount):
        user_obj = self.__user_dao.get_user(username)
        if user_obj.check_account(f'{account}') - (amount * 100) < 0:
            print("You do not have sufficient funds")
            return user_obj.__str__()
        return user_obj.withdraw(account, amount)

    def deposit(self, username, account, amount):
        user_obj = self.__user_dao.get_user(username)
        account_obj = None
        return user_obj.deposit(account, amount)

    def add_account(self, username, amount):
        user_obj = self.__user_dao.get_user(username)
        return user_obj.add_account(amount)
