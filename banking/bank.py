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
            
            
    def add_customer(self):
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        password = input("Enter Password: ")
        
        print("Choose account type: 1- checking\n 2- saving\n 3- Both")
        account_type = input("Enter Choice 1/2/3:")
        
        if self.customers:
            new_id = str(int(max(self.customers.keys())) + 1) 
        else:
            new_id = "10001"
            
        if account_type == "1":
            check = 0.0
            save = 0.0 
        elif account_type == "2":
            check = 0.0
            save = 0.0 
        else:
            check = 0.0
            save = 0.0 
    
        new_customer = Customer(
            account_id=new_id,
            Fname=fname,
            Lname=lname,
            password=password,
            check=check,
            save=save
        )
    
    
        self.customers[new_id] = new_customer 

        with open(self.csv_file, "a", newline='') as file:
            writer= csv.writer(file)
            writer.writerow([new_id, fname, lname, password, check, save]) 

        print(f"customer added successfully with ID: {new_id}")       
        
    