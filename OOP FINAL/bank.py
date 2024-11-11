class Bank:
    def __init__(self,name):
        self.name = name
        self.balance = 100000
        self.users = []
        self.admins = []
        self.loan = 0
        self.loanSys = True
        self.iniadmin = 101
        self.iniuser = 1001
    def addUser(self,user):
        user.accountNumber = self.iniuser
        self.iniuser += 1
        self.users.append(user)
    def addAdmin(self,admin):
        admin.adminId = self.iniadmin
        self.iniadmin += 1
        self.admins.append(admin)