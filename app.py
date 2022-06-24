from models.user import User


u1 = User("user1", 1001)

u1.add_account(789.2)
u1.add_account(1002)
print(u1)
print(u1.withdraw(1001001, 200.10))
print(u1.deposit(1001001, 200.05))




