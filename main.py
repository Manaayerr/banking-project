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
    
    action = input("Choose Action: 1- Deposite  2- Withdraw: ").strip()
    account_type = input("Choose Account [checking/savings]: ").lower().strip()
    amount = float(input("Enter an Amount: "))
    
    if action == "1":
        tran.deposit(account_type, amount)
    elif action == "2":
        tran.withdraw(account_type, amount)
    else:
        print(f"Invaild Action.")
    
    print(f"Update balances: checking: {customer.check}, savings: {customer.save}")
else:
        print("Invalid ID or Password")
        
add_new = input("Do you want to add new Customer? (y/n): ").lower()
if add_new == "y":
    bank.add_customer()
    bank.display_customers()

