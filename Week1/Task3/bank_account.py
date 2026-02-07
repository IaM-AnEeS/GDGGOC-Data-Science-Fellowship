class bankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount must be positive")
            return
        else:
            self.balance+=amount
            print(f"Deposited {amount}. New balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

class SavingsAccount(bankAccount):
    def __init__(self,account_number,account_holder,balance=0,interest_rate=0.04):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate=interest_rate
    
    def apply_interest(self):
        self.balance+=self.balance*self.interest_rate
        print(f"Applied interest. New balance is {self.balance}")
        
class CheckingAccount(bankAccount):
    def __init__(self,account_number,account_holder,balance=0,overdraft_limit=500):
        super().__init__(account_number,account_holder,balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self,amount):
        if amount>self.balance+self.overdraft_limit:
            print("Insufficient funds, overdraft limit exceeded")
        else:
            self.balance-=amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

savings= SavingsAccount("AN123","Anees",100000)
savings.deposit(5000)
savings.withdraw(2000)