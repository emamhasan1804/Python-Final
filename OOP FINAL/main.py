from user import User,Admin
from bank import Bank
ab = Bank('AB BANK')

def admin():
    adm = None
    while True:
        print('1. Login')
        print('2. Create Account')
        option = input("Enter your choice : ")
        if option == '1':
            adminId = int(input("Enter your admin id : "))
            for admin in ab.admins:
                if admin.adminId==adminId:
                    adm = admin
                    break
            if adm == None:
                print("Wrong admin id")
            else :
                break
        elif option =='2':
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            address = input("Enter your address : ")
            adm = Admin(name,email,address)
            ab.addAdmin(adm)
            break
        else :
            print("Wrong input")
    
    while True:
        print(f"\nWelcome {adm.name} your admin id : {adm.adminId}\n")
        print("1. Check Bank Balance")
        print("2. Check Loan Balance")
        print("3. See All Users")
        print("4. Delete User")
        print("5. On Loan System")
        print("6. Off Loan System")
        print("7. Exit")

        option = input("Enter your choice : ")
        if option == '1':
            adm.checkBalance(ab)
        elif option == '2':
            adm.checkLoan(ab)
        elif option == '3':
            adm.showUser(ab)
        elif option == '4':
            accountNumber = int(input("Enter user's accoount number : "))
            adm.removeUser(ab,accountNumber)
        elif option == '5':
            adm.onLoan(ab)
        elif option == '6':
            adm.offLoan(ab)
        elif option =='7':
            break
        else :
            print("\nWrong option")

def user():

    usr = None
    while True:
        print('1. Login')
        print('2. Create Account')
        option = input("Enter your choice : ")
        if option == '1':
            accountNumber = int(input("Enter your account Number : "))
            for user in ab.users:
                if user.accountNumber == accountNumber:
                    usr = user
                    break
            if usr == None:
                print("wrong account number")
            else :
                break
        elif option == '2':
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            address = input("Enter your address : ")
            accountType = input("Enter account type S - (savings) / C - (current) : (enter S/C) : ")
            accountType = accountType.lower()
            if accountType == 's':
                accountType = 'savings'
            elif accountType == 'c':
                accountType = 'current'
            else:
                print("Wrong account type. Enter (S/C)")
                continue
            usr = User(name,email,address,accountType)
            ab.addUser(usr)
            break
        else :
            print("wrong option")

    
    while True:
        print(f"\nWelcome {usr.name} your account number {usr.accountNumber}\n")
        print('1. Check Balance')
        print('2. deposit Balance')
        print('3. Withdraw Balance')
        print('4. Request Loan')
        print('5. Transaction History')
        print('6. Balance Transfer')
        print('7. Exit')

        option = input("Enter your choice : ")
        if option == '1':
            usr.checkBalance()
        elif option =='2':
            amount = int(input("Enter deposit amount : "))
            usr.deposit(ab,amount)
        elif option == '3':
            amount = int(input("Enter withdraw amount : "))
            usr.withdraw(ab,amount)
        elif option == '4':
            amount = int(input("Enter loan amount : "))
            usr.takeLoan(ab,amount)
        elif option == '5':
            usr.checkTransactionHistory()
        elif option == '6':
            receiverAccount = int(input("Enter receiver account number : "))
            amount = int(input("Enter Transfer amount : "))
            usr.transferBalance(ab,receiverAccount,amount)
        elif option == '7':
            break
        else :
            print("\nWrong option")


while True:
    print("\nWelcome to AB BANK\n")
    print('1. Admin')
    print('2. User')
    print('3. Exit')
    
    option = input("Enter your choice : ")
    if option == '1':
        admin()
    elif option == '2':
        user()
    elif option == '3':
        break
    else :
        print("\nWrong option")