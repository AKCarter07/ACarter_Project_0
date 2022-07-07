from dao.user_dao import UserDao
from dao.account_dao import AccountDao
from exception.invalid_parameter import InvalidParamError
from service.customer_service import CustomerService


class AccountService:
    def __init__(self):
        self.user_dao = UserDao()
        self.account_dao = AccountDao()
        self.cs = CustomerService()

    def get_accounts(self, user_id, dgt, dlt):
        user_obj = self.user_dao.get_user(user_id)
        accounts = user_obj.get_accounts()
        acct_list = {}
        for account in accounts:
            dollars = self.account_dao.get_account(account, user_id).get_dollars()
            if dgt != None and dlt != None:
                if dollars > int(dgt) and dollars < int(dlt):
                    acct_list.update({account: self.account_dao.get_account(account, user_id).to_dict()})
            elif dgt == None and dlt != None:
                if dollars < int(dlt):
                    acct_list.update({account: self.account_dao.get_account(account, user_id).to_dict()})
            elif dgt != None and dlt == None:
                if dollars > int(dgt):
                    acct_list.update({account: self.account_dao.get_account(account, user_id).to_dict()})
            else:
                acct_list.update({account: self.account_dao.get_account(account, user_id).to_dict()})
        return acct_list

    def get_account(self, user_id, account_number):
        if f'{user_id}' not in self.cs.user_id_list():
            raise InvalidParamError(f"User Id does not exist.")
        elif f'{account_number}' not in self.user_dao.get_user(user_id).get_accounts():
            raise InvalidParamError(f"Account {account_number} not found.")
        else:
            return self.account_dao.get_account(account_number, user_id).to_dict()

    def withdraw(self, user_id, account_id, dollars, cents):
        user_obj = self.user_dao.get_user(user_id)
        if f'{account_id}' not in user_obj.get_accounts():
            raise InvalidParamError(f"Account {account_id} not found.")
        elif user_obj.check_account(f'{account_id}') - ((dollars * 100) + cents) < 0:
            raise InvalidParamError(f"You do not have sufficient funds.")
        else:
            account_object = self.account_dao.edit_account(account_id, user_id, 'withdraw', dollars, cents)
            return f"New balance: {account_object}"

    def deposit(self, user_id, account_id, dollars, cents):
        user_obj = self.user_dao.get_user(user_id)
        if f'{account_id}' not in user_obj.get_accounts():
            raise InvalidParamError(f"Account {account_id} not found.")
        else:
            account_object = self.account_dao.edit_account(account_id, user_id, 'deposit', dollars, cents)
            return f"New balance: {account_object}"

    def add_account(self, user_id, dollars, cents):
        user_obj = self.user_dao.get_user(user_id)
        num_accounts = user_obj.get_num_accounts()+1
        num_active_accounts = user_obj.get_num_active_accounts() + 1
        account_id = f"{user_id}00{'0'if num_accounts < 10 else ''}{num_accounts}"
        result = self.account_dao.create_account(user_id, account_id, dollars, cents)
        user_obj.set_total_accounts(num_accounts)
        user_obj.set_num_active_accounts(num_active_accounts)
        self.user_dao.edit_user(user_id, user_obj)
        return result
    def delete_account(self, user_id, account_id):
        user_obj = self.user_dao.get_user(user_id)
        if f'{user_id}' not in self.cs.user_id_list():
            raise InvalidParamError(f"User Id does not exist.")
        if f'{account_id}' not in user_obj.get_accounts():
            raise InvalidParamError(f"Account {account_id} not found.")
        else:
            user_obj.set_num_active_accounts(user_obj.get_num_active_accounts() - 1)
            self.user_dao.edit_user(user_id, user_obj)
            return self.account_dao.delete_account(user_id, account_id)
