class Account:
    def __init__(self, name, balance=0):
        self.name = name 
        self.balance = balance
        if self.balance < 0:
            print(f"[WARNING:] You cannot enter a negative number in {self.name}'s balance!\n[WARNING:] We've reset {self.name} balance to 0$!")
            self.balance = 0 # reset balance

    def my_bal(self):
        print(f"{self.name}'s balance: {self.balance}$")

    def deposit(self, amount):
        if amount <= 0:
            print(f"[WARNING:] Please enter a positive integer")
            return False
        self.balance += amount
        print(f"[SUCCEED:] {self.name} deposits {amount}$")
        return True 
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"[WARNING:] {self.name} don't have enough balance to withdraw")
            return False
        self.balance -= amount
        print(f"[SUCCEED:] {self.name} withdraws {amount}$")
        return True
    
    def transfer(self, amount, target):
        if amount <= 0:
            print("[WARNING:] Enter a number that is more than 0$")
            return False
        if self.withdraw(amount):
            target.deposit(amount)
            print(f"[SUCCEED:] {self.name} transfered {amount}$ to {target.name}'s balance!")
            return True
        else:        
            return False

class Bank:
    def __init__(self, b_name):
        self.b_name = b_name
        self.data_base = {} 
    def open_acc(self, owner, init_bal=0):
        self.owner = Account(owner, init_bal)
        self.data_base[self.owner.name] = self.owner # to have a account in bank's data base with a searchable key
        print(f"{self.owner.name} account open succeed!")
        return True
    def find_acc(self, to_find):
        if not self.data_base.get(to_find):
            print(f"[WARNING:] No username called '{to_find}' in the bank!")
            return False
        found = self.data_base.get(to_find) # note: this is an obj
        print(f"[SUCCEED:] Found user: '{found}'")

bank = Bank("Taiwan-Central-Bank")
mike = Account("Mike", 10000)
ryan = Account("Ryan", 1000) # he's poor
nico = Account("Nico", -550) # test 
jenson = bank.open_acc("Jenson")
gura = bank.open_acc("Gura")

mike.transfer(6767, ryan)

mike.my_bal()
ryan.my_bal()
nico.my_bal()

print(bank.data_base)
bank.find_acc("yoyo")
bank.find_acc("Gura")
bank.find_acc("Miki")

