class Account:

    def __init__(self, acct_num, start_dollars, start_cents):
        self.__account_number = str(acct_num)
        self.__balance_dollars = int(start_dollars)
        self.__balance_cents = int(start_cents)

    def deposit(self, dollars, cents):
        curr_bal = (self.__balance_dollars * 100) + self.__balance_cents
        new_bal = int(curr_bal + (dollars * 100) + cents)
        self.__balance_dollars = int(new_bal // 100)
        self.__balance_cents = int(new_bal % 100)
        return (f"You deposited ${dollars}.{'0' if cents < 10 else ''} to account "
                f"{self.__account_number}. Your new balance is ${self.__balance_dollars:,}."
                f"{'0' if self.__balance_cents < 10 else ''}{self.__balance_cents}")

    def withdraw(self, dollars, cents):
        curr_bal = (self.__balance_dollars * 100) + self.__balance_cents
        new_bal = int(curr_bal - ((dollars * 100) + cents))
        self.__balance_dollars = int(new_bal // 100)
        self.__balance_cents = int(new_bal % 100)
        return (f"You withdrew ${dollars}.{cents} from account {self.__account_number}. "
                f"Your new balance is ${self.__balance_dollars:,}."
                f"{'0' if self.__balance_cents < 10 else ''}{self.__balance_cents}")

    def query(self):
        return (self.__balance_dollars * 100) + self.__balance_cents

    def __str__(self):
        return (f"Account {self.__account_number}: Balance ${self.__balance_dollars:,}."
                f"{'0' if self.__balance_cents < 10 else ''}{self.__balance_cents}")

    def to_dict(self):
        return {
            'account number': self.__account_number,
            'dollars': self.__balance_dollars,
            'cents': self.__balance_cents
        }

    def get_dollars(self):
        return self.__balance_dollars

    def get_cents(self):
        return self.__balance_cents

    def get_account_num(self):
        return self.__account_number
