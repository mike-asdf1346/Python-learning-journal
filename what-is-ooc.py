# Object-oriented-programming, also known as OOC, whcih we treat every objects here as real-world object
# Article source: FreeCodeCamp 'What Is Object-Oriented Programming, and How Does Encapsulation Work?'
class Pc: 
    def __init__(self, ram, storage, gpu, cpu):
        self.ram = ram 
        self.storage = storage 
        self.gpu = gpu
        self.cpu = cpu

my_pc = Pc("16GB", "1TB", "Nvidia", "Intel") # an obj
# print(my_pc.cpu) # my_pc ram: 16GB

# ooc has a key principle which is, encapsulation, polymorphism, inheritance and abstraction

# encapsulation(封裝): to pack informations together and hide the details of the code running behind the scene to enhance the security.
# polymorphism(多形): expressing various of acts towards different informations, with a single interface or panel  
# inheritance(繼承): has parent class and child class, parent can pass down information to child, so that child can use what the parent gives, which reduces the repetitive code
# abstraction(抽象): hide the detail, express core functions and outer layers

class Account:
    # principles of encapsulation
    def __init__(self, name, bal=0): # bal = balance
        self.name = name
        self._bal = bal # '_' no one should access from outside of the class
    def deposit(self, amount):
        if amount < 0:
            print("Enter a positive integer")
            return False
        self._bal += amount
        print(f"{self.name} deposits: {amount}$")
        return True
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

class Bank_Account:
    def __init__(self, name, bal=0): # bal = balance
        self.name = name
        self.__bal = bal # private attribute
    def deposit(self, amount):
        if amount < 0:
            print("Enter a positive integer")
            return False
        self.__bal += amount
        print(f"{self.name} deposits: {amount}$")
        return True
    def withdraw(self, amount):
        if 0 < amount <= self.__bal:
            self.__bal -= amount
# __bal = _Wallet_balance__balance, less name collision, harder to access by accident though it is not strictly lockdown


