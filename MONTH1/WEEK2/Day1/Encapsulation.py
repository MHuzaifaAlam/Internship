class Wallet:
    def __init__(self,balance):
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
    def  withdraw(self,amount):
        if 0<amount <= self._balance:
            self._balance-=amount
    def get_bal(self):
        return self._balance


acct_one=Wallet(50)
acct_one.deposit(100)
print(f"Balance {acct_one.get_bal()}")
acct_one.withdraw(20)
print(f"Current bal after withdarw is : {acct_one.get_bal()}")