from models.account import Account


class User:
    def __init__(self, username, idn):
        self.__username = username
        self.__idn = idn
        self.__password = "password"
        self.__num_accounts = 0
        self.__user_accounts = {}

    def set_password(self):
        new_pass_1 = '1'
        new_pass_2 = '2'
        if input("Old password: ") == self.__password:
            while new_pass_1 != new_pass_2:
                new_pass_1 = input("New password: ")
                new_pass_2 = input("Confirm new password: ")
                if new_pass_1 != new_pass_2:
                    print("Passwords do not match")
        elif input("Incorrect password \n Old password: ") == self.__password:
            pass
        else:
            print("Please contact customer support for help resetting your password")

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
        line = (f"\n{self.__username} ({self.__idn}) has {self.__num_accounts} account"
                f"{'s' if self.__num_accounts > 1 or self.__num_accounts == 0 else ''}: \n")
        count = 0
        for key in self.__user_accounts:
            count += 1
            new = f"{self.__user_accounts.get(key)}"
            if count < self.__num_accounts:
                cr = "\n"
            else:
                cr = ""
            line = line + new + cr
        return line

    def to_dict(self):
        accounts = []
        for key in self.__user_accounts:
            accounts.append(self.__user_accounts.get(key).to_dict())
        return {
            "username": self.__username,
            "ID Number": self.__idn,
            "password": self.__password,
            "number of accounts": self.__num_accounts,
            "user accounts": accounts
        }
