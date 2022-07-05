from models.account import Account


class User:
    def __init__(self, username, idn):
        self.__username = username
        self.__idn = idn
        self.__num_active_accounts = 0
        self.__num_accounts = 0
        self.__user_accounts = {}
        self.__active = True

    def add_account(self, start_balance):
        self.__num_active_accounts += 1
        self.__num_accounts += 1
        account_id = f"{self.__idn}00{'0' if self.__num_accounts < 10 else ''}{self.__num_accounts}"
        account = Account(account_id, start_balance)
        self.__user_accounts.update({account_id: account})
        return f"You have added account {account_id} with amount {start_balance:.2f}."

    def close_account(self, account):
        self.__user_accounts.pop(account)

    def __str__(self):
        line = (f"\n{self.__username} ({self.__idn}) has {self.__num_active_accounts} active account"
                f"{'s' if self.__num_active_accounts > 1 or self.__num_active_accounts == 0 else ''}: \n")
        count = 0
        for key in self.__user_accounts:
            count += 1
            new = f"{self.__user_accounts.get(key)}"
            if count < self.__num_active_accounts:
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
            "user_id": self.__idn,
            "num_active_accounts": self.__num_active_accounts,
            "active": self.__active
        }

    def get_username(self):
        return self.__username

    def get_idn(self):
        return self.__idn

    def check_account(self, account):
        return self.__user_accounts[account].query()

    def set_num_active_accounts(self, num):
        self.__num_active_accounts = num

    def set_total_accounts(self, num):
        self.__num_accounts = num

    def set_status(self, status):
        self.__active = status

    def set_accounts(self, accounts_list):
        for account in accounts_list:
            account_object = Account(account[2], account[3], account[4])
            self.__user_accounts[account[2]] = account_object

    def get_num_accounts(self):
        return self.__num_accounts

    def get_num_active_accounts(self):
        return self.__num_active_accounts

    def get_status(self):
        return self.__active

    def get_accounts(self):
        return self.__user_accounts

