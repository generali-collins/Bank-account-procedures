
#task1
class BankAccount:
    def __init__(self,accNo):
        self.accNo=accNo
        self.balance=0
        self.noWithdrawals=0
        self.noDeposits=0
        
    def deposit(self,depAmount):
        self.depAmount=depAmount
        self.balance=self.balance+self.depAmount

        self.noDeposits=self.noDeposits+1
        
    def withdraw(self,withD,purpose):
        self.withD=withD
        self.purpose=purpose
        if self.withD<=self.balance:
            self.balance=self.balance-self.withD
            self.noWithdrawals=self.noWithdrawals+1
            print("Congratulations Withdrawal Successful!")
            print("You have withdrawn US$"+str(withD)+" for ",str(self.purpose),".")
        else:
            print("Aw sorry, Withdrawal Failed!")
            print("Insufficient Balance!")

    def checkBalance(self):
        print("Your Balance is: ",self.balance)

    def accountHistory(self):
        print("You have deposited ",self.noDeposits,"times into your bank accout ",self.accNo)
        print("You have withdrwan ",self.noWithdrawals," times out of your bank accout ",self.accNo)
