class Account:
    def __init__(self, acct_num, start_balance):
        self.__account_number = acct_num
        self.__balance_dollars = int(start_balance)
        self.__balance_cents = int(((start_balance * 1000) / 10)% 100)

    def deposit(self, amount):
        curr_bal = (self.__balance_dollars * 100) + self.__balance_cents
        new_bal = int(curr_bal + (amount * 100))
        self.__balance_dollars = int(new_bal // 100)
        self.__balance_cents = int(new_bal % 100)
        return (f"You deposited ${amount:.2f}. "
                f"Your new balance is ${self.__balance_dollars:,}."
                f"{'0' if self.__balance_cents < 10 else ''}{self.__balance_cents}")

    def withdraw(self, amount):
        curr_bal = (self.__balance_dollars * 100) + self.__balance_cents
        new_bal = int(((curr_bal * 10) - (amount * 1000))/10)
        self.__balance_dollars = int(new_bal // 100)
        self.__balance_cents = int(new_bal % 100)
        return (f"You withdrew ${amount:.2f}. "
                f"Your new balance is ${self.__balance_dollars:,}."
                f"{'0' if self.__balance_cents < 10 else ''}{self.__balance_cents}")

    def query(self):
        return((self.__balance_dollars * 100) + self.__balance_cents)

    def __str__(self):
        return (f"Account {self.__account_number}: Balance ${self.__balance_dollars:,}."
                f"{'0' if self.__balance_cents < 10 else ''}{self.__balance_cents}")
