from datetime import datetime

class Person:
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address

class User(Person):
    def __init__(self, name, email, address,accountType):
        self.accountType = accountType
        self.accountNumber = None
        self.balance = 0
        self.history = []
        self.loan = 0
        self.loanCount = 0
        super().__init__(name, email, address)
    
    def deposit(self,bank,amount):
        self.balance += amount
        bank.balance += amount
        transHis = f"deposit - {amount}TK - {datetime.now()}"
        self.history.append(transHis)
        print(f'{amount} TK deposited')

    def withdraw(self,bank,amount):
        if amount>self.balance:
            print("Withdrawal amount exceeded")
        elif amount>bank.balance:
            print("Bank is bankrupt")
        else:
            self.balance -= amount
            bank.balance -= amount
            transHis = f"withdraw - {amount}TK - {datetime.now()}"
            self.history.append(transHis)
            print(f'{amount} TK withdraw successfull')
    
    def checkBalance(self):
        print(f'Account Balance : {self.balance}TK')
    
    def checkTransactionHistory(self):
        print("----- Transaction -----")
        for item in self.history:
            print(item)
    
    def takeLoan(self,bank,amount):
        if bank.loanSys == False:
            print("Loan system is currently not available")
            return
        if self.loanCount == 2:
            print("You can't take lone more than two times")
        else:
            if amount>bank.balance:
                print("Insufficient Balance in Bank")
            else :
                self.loanCount +=1
                self.loan += amount
                self.balance += amount
                bank.loan += amount
                transHis = f"loan - {amount} TK - {datetime.now()}"
                self.history.append(transHis)
                print(f'Your account has been credited with {amount} TK as a loan')

    def transferBalance(self,bank,receiverAccount,amount):
        flag = False
        for user in bank.users:
            if user.accountNumber == receiverAccount:
                flag = True
                if self.balance<amount:
                    print("Insufficient Balance")
                else :
                    self.balance -= amount
                    user.balance += amount
                    print(f"{amount} TK is transferred to acount no {receiverAccount}")
                    his = f"Transfer - {amount} TK - {datetime.now()}"
                    self.history.append(his)
                    his = f"Receive - {amount} TK - {datetime.now()}"
                    user.history.append(his)
                break
        if flag == False:
            print("No user found with the given account number")
    
class Admin(Person):
    def __init__(self, name, email, address):
        self.adminId = None
        super().__init__(name, email, address)
    
    def showUser(self,bank):
        print("----- Users -----")
        print("Name\tAccount Number\tEmail")
        for user in bank.users:
            print(f"{user.name}\t{user.accountNumber}\t{user.email}")
    
    def checkBalance(self,bank):
        print(f"Vault Balance : {bank.balance} TK")
    
    def checkLoan(self,bank):
        print(f'Loan given : {bank.loan} TK')
    
    def onLoan(self,bank):
        if bank.loanSys == True:
            print("Loan system is already on")
        else :
            print("Loan system is on from now")
            bank.loanSys = True
    def offLoan(self,bank):
        if bank.loanSys == False:
            print("Loan system is already off")
        else :
            print("Loan system is off from now")
            bank.loanSys = False

    def removeUser(self,bank,accountNumber):
        flag = False
        for user in bank.users:
            if user.accountNumber == accountNumber:
                flag = True
                bank.users.remove(user)
                print(f'User account with account number {accountNumber} is deleted')
                break
        if flag == False:
            print('No user found')
    