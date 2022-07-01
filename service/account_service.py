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

    def withdraw(self, user_id, account_id, dollars, cents):
        user_obj = self.__user_dao.get_user(user_id)
        print(f"In Withdraw.")
        if f'{account_id}' not in user_obj.get_accounts():
            raise InvalidParamError(f"Account {account_id} not found.")
        elif user_obj.check_account(f'{account_id}') - ((dollars * 100) + cents) < 0:
            print("You do not have sufficient funds")
            return user_obj.__str__()
        else:
            self.__account_dao.edit_account(account_id, user_id, 'withdraw', dollars, cents)
            account_object = self.__account_dao.get_account(account_id, user_id)
            return f"New balance: {account_object}"

    def deposit(self, user_id, account_id, dollars, cents):
        user_obj = self.__user_dao.get_user(user_id)
        print(f"In Deposit.")
        if f'{account_id}' not in user_obj.get_accounts():
            raise InvalidParamError(f"Account {account_id} not found.")
        else:
            self.__account_dao.edit_account(account_id, user_id, 'deposit', dollars, cents)

            account_object = self.__account_dao.get_account(account_id, user_id)
            return f"New balance: {account_object}"

    def add_account(self, user_id, dollars, cents):
        user_obj = self.__user_dao.get_user(user_id)
        num_accounts = user_obj.get_num_accounts()+1
        account_id = f"{user_id}00{'0'if num_accounts < 10 else ''}{num_accounts}"
        result = self.__account_dao.create_account(user_id, account_id, dollars, cents)
        user_obj.set_num_accounts(num_accounts)
        self.__user_dao.edit_user(user_id, user_obj)
        return result

    def delete_account(self, user_id, account_id):
        user_obj = self.__user_dao.get_user(user_id)
        print(f"In Delete_Account.")
        if f'{account_id}' not in user_obj.get_accounts():
            raise InvalidParamError(f"Account {account_id} not found.")
        else:
            user_obj.set_num_accounts(user_obj.get_num_accounts()-1)
            self.__user_dao.edit_user(user_id, user_obj)
            return self.__account_dao.delete_account(user_id, account_id)
