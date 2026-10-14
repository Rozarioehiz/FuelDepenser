class Account:
    def __init__(self, name: str)-> None:
        self.name = name.lower()
        self.balance = 0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Amount exceeds balance")
        self.balance -= amount


# acc = Account("Bob")
# acc1 = Account("Alice")
# print(acc.balance)











