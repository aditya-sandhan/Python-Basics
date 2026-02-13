'''Create a BankAccount class with attributes account_number, owner_name, and balance.
Add methods to deposit, withdraw, and check_balance'''


class BankAccount:
    
    def __init__(self, account_number, owner_name):
        self.acc_no = account_number
        self.name = owner_name
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} Deposited!")

    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print(f"{amount} is withdrawn!")

    def check_balance(self):
       
        print(f"Balance ={self.balance} ")

b1 = BankAccount(101, "Aditya")
b1.deposit(50000)
b1.withdraw(2000)
b1.check_balance()

print()

b2 = BankAccount(101, "Vaishnavi")
b2.deposit(100000)
b2.withdraw(35000)
b2.check_balance()