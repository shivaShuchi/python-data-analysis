import random

print("BANK ACCOUNT SYSTEM".center(100,"-"))
accounts = {}

def create_account():
    number = int(random.randint(1000000000, 9999999999))
    if number not in accounts:
        account_no = no
    account_balance = 0
    print("Fill your details")
    name = input("Account Holder Name:")
    print(f"Your account number will be {account_no}")
    print("Minimum balance is 10000, depositing 10000")
    account_balance += 10000
    accounts[account_no] = {"name" : name,  "balance" : account_balance}
    print("Account created successfully!")

def deposit(account_no):
    if account_no in accounts:
        amount = int(input("Enter amount to be deposited:"))
        accounts[account_no]["balance"] += amount
        print(f"{amount} deposited")
    else:
        print("You don't have an account!")

def withdraw(account_no):
    if account_no in accounts:
        amount = int(input("Enter amount to be withdrawn:"))
        balance = accounts[account_no]["balance"]
        if balance >= amount:
            accounts[account_no]["balance"] -= amount
            print(f"{amount} withdrawn")
        else:
            print("Not enough balance")
    else:
        print("You don't have an account!")

def check(account_no):
    if account_no in accounts:
        print("Your account balance is:")
        print(accounts[account_no]["balance"])
    else:
        print("You don't have an account!")


while True:
    choice = int(input(
        """Choose:
        1. Create Account
        2. Deposit Money
        3. Withdraw Money
        4. Check Balance
        5. Exit
        """
    ))
    if choice == 1:
        create_account()
    elif choice == 2:
        acc_no = int(input("Enter your account no:"))
        deposit(acc_no)
    elif choice == 3:
        acc_no = int(input("Enter your account no:"))
        withdraw(acc_no)
    elif choice == 4:
        acc_no = int(input("Enter your account no:"))
        check(acc_no)
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
