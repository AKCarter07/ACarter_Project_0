from models.account import Account


a1 = Account(1001, 10000.8)
print(a1)

print(a1.deposit(200))
print(a1.deposit(0.30))
print(a1.deposit(0.45))
print(a1.withdraw(100.50))

print(a1.query())



