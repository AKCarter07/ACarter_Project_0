from models.account import Account


class User:
    def __init__(self, username, idn):
        self.username = username
        self.idn = idn
        self.num_active_accounts = 0
        self.num_accounts = 0
        self.user_accounts = {}
        self.active = True

    def add_account(self, dollars, cents):
        self.num_active_accounts += 1
        self.num_accounts += 1
        account_id = f"{self.idn}00{'0' if self.num_accounts < 10 else ''}{self.num_accounts}"
        account = Account(account_id, dollars, cents)
        self.user_accounts.update({account_id: account})
        return f"You have added account {account_id} with amount ${dollars}." \
               f"{'0' if cents < 10 else ''}{cents}"

    def close_account(self, account):
        self.user_accounts.pop(account)

    def __str__(self):
        line = (f"\n{self.username} ({self.idn}) has {self.num_active_accounts} active account"
                f"{'s' if self.num_active_accounts > 1 or self.num_active_accounts == 0 else ''}: \n")
        count = 0
        for key in self.user_accounts:
            count += 1
            new = f"{self.user_accounts.get(key)}"
            if count < self.num_active_accounts:
                cr = "\n"
            else:
                cr = ""
            line = line + new + cr
        return line

    def to_dict(self):
        accounts = []
        for key in self.user_accounts:
            accounts.append(self.user_accounts.get(key).to_dict())
        return {
            "username": self.username,
            "user_id": self.idn,
            "num_active_accounts": self.num_active_accounts,
            "active": self.active
        }

    def get_username(self):
        return self.username

    def get_idn(self):
        return self.idn

    def check_account(self, account):
        return self.user_accounts[account].query()

    def set_num_active_accounts(self, num):
        self.num_active_accounts = num

    def set_total_accounts(self, num):
        self.num_accounts = num

    def set_status(self, status):
        self.active = status

    def set_accounts(self, accounts_list):
        for account in accounts_list:
            account_object = Account(account[2], account[3], account[4])
            self.user_accounts[account[2]] = account_object

    def get_num_accounts(self):
        return self.num_accounts

    def get_num_active_accounts(self):
        return self.num_active_accounts

    def get_status(self):
        return self.active

    def get_accounts(self):
        return self.user_accounts

