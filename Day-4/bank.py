class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ₹{amount}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance!")
        return self.__balance

    def get_balance(self):
        return self.__balance


account = BankAccount(3000)   

account.deposit(5000)         
account.withdraw(2000)       
print("Current Balance: ₹", account.get_balance())


class BankAccount:
    def _init_(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")

    def get_balance(self):
        return self.__balance
print("====uaing inheritence====")

class SBI(BankAccount):
    def _init_(self, balance=0):
        super()._init_(balance)  

acc = BankAccount(0)
acc.deposit(5000)
acc.withdraw(2000)
print("Final balance:", acc.get_balance())


sbi_acc = SBI(1000)
sbi_acc.deposit(2000)
sbi_acc.withdraw(500)
print("SBI account balance:", sbi_acc.get_balance())