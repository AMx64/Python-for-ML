import time

class Bankaccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    @property 
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance amount cannot be negative\n")
        self.__balance = amount

    def withdraw(self, amount):
        if amount < 0:
            print("Current Balance: ", self.__balance)
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.__balance:
            print("Current Balance: ", self.__balance)
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        print("Current Balance: ", self.__balance)

    def deposit(self, amount):
        if amount < 0:
            print("Current Balance: ", self.__balance)
            raise ValueError("Deposit amount cannot be negative")
        self.__balance += amount
        print("Current Balance: ", self.__balance)

    def check_balance(self):
        print("Current Balance: ", self.__balance)
    
a = 0
print("\nWelcome to AMx64 Banking system. Let's get you started with your current account")
account = Bankaccount()

while True:
    try:
        amt = int(input("Enter an amount to deposit: "))
        account.balance = amt
        break
    except ValueError as ve:
        print(f"Invalid input: {ve}")

while a!= 4:
    print("\n--- Menu ---")
    print("Enter 1 to view current balance")
    print("Enter 2 to deposit amount")
    print("Enter 3 to withdraw amount")
    print("Enter 4 to exit")
    while True:
        try:
            a = int(input("Enter key: "))
            if a >= 1 and a <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input: Please enter a valid intege between 1 and 4.")
    if a == 1:
        account.check_balance()
    elif a == 2:
        time.sleep(0.5)
        try:
            value = int(input("Enter amount to deposit: "))
            account.deposit(value)
        except ValueError as ve:
            print(f"ValueError: {ve}")
    elif a == 3:
        time.sleep(0.5)
        try:
            value = int(input("Enter amount to withdraw: "))
            account.withdraw(value)
        except ValueError as ve:
            print(f"ValueError: {ve}")

    time.sleep(0.5)

print("Thank you for banking with us")