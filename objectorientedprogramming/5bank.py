class Bank:
    acno:int
    balance:int
    ac_type:str
    customer_name:str

    def __init__(self,acno,balance,ac_type,customer_name):
        self.acno=acno
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"your account {self.acno} has been credited with amount {amount}avl bal{self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print("insuffient balance")
        else:
            
            self.balance=self.balance-amount
            print(f"your account {self.acno} has been debited with amount {amount}avl bal{self.balance}")
        
    def get_balance(self):
        print("your avl balance",self.balance)

account_instance=Bank(12345,1000,"saving","krishna")
account_instance.deposit(1000)
account_instance.withdraw(500)