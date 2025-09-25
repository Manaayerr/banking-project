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
    
    action = input("Choose Action: 1- Deposite  2- Withdraw 3- Transfer: ").strip()
    account_type = input("Choose Account [checking/savings]: ").lower().strip()
    amount = float(input("Enter an Amount: "))
    
    if action == "1":
        tran.deposit(account_type, amount)
    elif action == "2":
        tran.withdraw(account_type, amount)
    elif action == "3":
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

