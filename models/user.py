from models.account import Account


class User:
    def __init__(self, username, idn):
        self.__username = username
        self.__idn = idn
        self.__num_accounts = 0
        self.__user_accounts = {}

    def add_account(self, start_balance):
        self.__num_accounts += 1
        account_id = f"{self.__idn}0{'0' if self.__num_accounts < 10 else ''}{self.__num_accounts}"
        account = Account(account_id, start_balance)
        self.__user_accounts.update({account_id: account})

    def close_account(self, account):
        self.__user_accounts.pop(account)

    def withdraw(self, account, amount):
        return self.__user_accounts[f'{account}'].withdraw(amount)

    def deposit(self, account, amount):
        return self.__user_accounts[f'{account}'].deposit(amount)

    def __str__(self):
        line = f"{self.__username} ({self.__idn}) has {self.__num_accounts} accounts: \n"
        for key in self.__user_accounts:
            new = f"{self.__user_accounts.get(key)}"
            line = line + new + "\n"
        return line
