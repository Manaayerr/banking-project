import csv 
from banking.customer import Customer

class Bank:
    def __init__(self, csv_file="banking/bank.csv"):
        self.csv_file = csv_file
        self.customers = self.load_customers()
        
        
    def load_customers(self):
        customers = {}
        try:
            with open(self.csv_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    c= Customer(
                        account_id=row['account_id'],
                        Fname=row['frst_name'],
                        Lname=row['last_name'],
                        password=row['password'],
                        check=row['balance_checking'],
                        save=row['balance_savings']
                    )
                    customers[c.account_id] = c
        except FileNotFoundError:
            print('CSV file not found')
        return customers


    def display_customers(self):
        print("Customers \n")
        for c in self.customers.values():
            print(c)
    
    