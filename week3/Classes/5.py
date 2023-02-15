class BankAccount:
    def __init__(self, name):
        self.owner=name
        self.balance=0
    def deposit(self, x):
        self.balance+=x
        print("Current balance:{}$".format(self.balance))
    def withdraw(self,x):
        if(x>self.balance):
            print("{}, you have no enough balance for the withdrawal!".format(self.owner))
        else:
            self.balance-=x
            print("{}$ withdrawed succesfully".format(x))
            print("Current balance:{}$".format(self.balance))

acc=BankAccount("Magzhan")
acc.deposit(450)
acc.withdraw(1200)
acc.deposit(10000)
acc.withdraw(8000)