from time import sleep as t
class Account:
    def __init__(self, name, bal=0):
        self.name = name
        self._bal = bal
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Invalid type ---> 'name'")
        self._name = new_name

    @property
    def bal(self):
        if self._bal < 0:
            raise AttributeError("Enter at least equal or more than $0")
        return self._bal

    @bal.setter
    def bal(self, target):
        self.check_zero(target)
        self._bal = target

    def deposit(self, amount):
        self.check_zero(amount)
        self.bal += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        self.check_zero(amount)
        if amount > self.bal:
            raise ValueError("You have no money left")
        self.bal -= amount
        return f"Withdrew: -${amount}"

    def show_bal(self):
        return f"---------------------------\nYour balance: ${self.bal}\n---------------------------"
    
    def check_zero(self, value): # checker: checks if target number is equal or less than 0
        if not isinstance(value, int):
            raise TypeError("Please at least enter a integer")
        if value <= 0:
            raise ValueError("You cannot enter a number that is equal to 0 or below")

        return None

mike = Account('Mike', 1000) # creates a new obj
mike.name = "Jelly Pie"
mike.bal = 6000
print(mike.name)

for _ in range(100): # costs you 67
    print(mike.withdraw(67))
    print(mike.show_bal())
    t(0.1)

# for _ in range(100): # grants you 67
#     print(mike.withdraw(67))
#     print(mike.show_bal())
#     t(0.1)