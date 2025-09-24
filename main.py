import csv 
from banking.customer import Customer
from banking.bank import Bank

csv_file = "banking/bank.csv"

try:
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer=Customer(
            account_id=row["account_id"],
            Fname=row['frst_name'],
            Lname=row['last_name'],
            password=row['password'],
            check=row['balance_checking'],
            save=row['balance_savings']
            )
        print(customer)
except FileNotFoundError:
    print('File not found!')

    
bank = Bank()
bank.display_customers()

# bank.add_customer()
bank.display_customers()

print("Login\n")
account_id = input("Enter Account ID: ")
password = input("Enter Password: ")

customer= bank.login(account_id, password)

if customer:
    print(f"Welcome, {customer.Fname} {customer.Lname}!")
else:
    print(f"Invaild ID or Password.")