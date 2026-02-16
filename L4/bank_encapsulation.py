class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute can only be accessed with setter and getter methods

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")

   
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(5000)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # AttributeError: private attribute
