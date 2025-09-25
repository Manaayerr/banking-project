import csv 
from banking.customer import Customer
from banking.bank import Bank
from banking.bank import Transaction

bank = Bank()
bank.display_customers() 

print("Login\n")
account_id = input("Enter Account ID: ").strip()
password = input("Enter Password: ").strip()

customer= bank.login(account_id, password)

if customer:
    print(f"Welcome, {customer.Fname} {customer.Lname}!")
    tran= Transaction(customer, bank)
    
    print("Choose Action:\n 1-Deposit\n 2- Withrraw\n 3- Transfer")
    action = input("Enter choose: ").strip()
    
    if action == "1":
        account_type = input("Choose Account [checking/savings]: ").lower().strip()
        amount = float(input("Enter an Amount: "))
        tran.deposit(account_type, amount)
        
    elif action == "2":
        account_type = input("Choose Account [checking/savings]: ").lower().strip()
        amount = float(input("Enter an Amount: "))
        tran.withdraw(account_type, amount)
        if not customer.is_active:
            print("Account deactivated due to overdrafts")
            re =float(input(" Enter amount to reactivate: "))
            bank.reactivate_account(customer,re)
            
    elif action == "3":
        account_type = input("Choose Account [checking/savings]: ").lower().strip()
        target_id = input("enter target account ID for transfer: ").strip()
        target_account_type = input("target account [checking/savings]: ").lower().strip()
        amount = float(input("Enter amount to transfer: "))
        target_customer = bank.customers.get(target_id)
        tran.transfer(account_type,target_account_type,amount,target_customer)
    else:
        print(f"Invaild Action.")
    
    print(f"Update balances: checking: {customer.check}, savings: {customer.save}")
else:
        print("Invalid ID or Password")
        
add_new = input("Do you want to add new Customer? (y/n): ").lower()
if add_new == "y":
    bank.add_customer()
    bank.display_customers()

