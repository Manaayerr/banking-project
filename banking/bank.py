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
        
    def login(self,account_id,password):
        if account_id in self.customers:
            customer = self.customers[account_id]
            if customer.password == password:
                return customer
        return None
    
    def update_csv(self,customer):
        try:
            with open(self.csv_file, "w" , newline='') as file:
                fieldnames = ['account_id','frst_name','last_name','password','balance_checking','balance_savings']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for c in self.customers.values():
                    writer.writerow({
                        'account_id': c.account_id,
                        "frst_name": c.Fname,
                        'last_name': c.Lname,
                        'password': c.password,
                        'balance_checking': c.check,
                        'balance_savings': c.save
                    })
        except Exception as err:
            print(f"Error updating csv: {err}")
            
    def reactivate_account(self,customer,payment):
        if not customer.is_active:
            customer.check += float(payment)
            customer.overdraft_count = 0
            customer.is_active = True
            print(f"Account {customer.account_id} reactivated")
            self.update_csv(customer)
            
class Transaction:
    def __init__(self,customer, bank):
        self.customer = customer
        self.bank = bank
        
    def deposit(self,account_type,amount):
        amount = float(amount)
        if account_type == 'checking':
            self.customer.check += amount
            print(f"new checking blance: {self.customer.check}")
        elif account_type == "savings":
            self.customer.save += amount
            print(f"new savings balance: {self.customer.save}")
        else:
            print("Invaild account type")
            return
        
        self.bank.update_csv(self.customer)
        
    def withdraw(self,account_type, amount):
        # overdraft
        if not self.customer.is_active:
            print("this account is deactivated due to overdraft limits.")
            return
        
        amount = float(amount)
        
        if account_type == "checking":
            balance = self.customer.check
        elif account_type == "savings":
            balance=self.customer.save 
        else:
            print("Invaild account type")
            return
        if balance - amount < -100:
            print("cannot withdraw, would exceed allowed overdraft of -$100")
            self.customer.is_active = False
            self.customer.overdraft_count += 1
            self.bank.update_csv(self.customer)
            return
        
        if balance <0 and amount > 100:
            print("Can not withdraw more than $100 when account is negative")
            return
        
        new_balance = balance - amount
        
        if new_balance < 0:
            self.customer.overdraft_count += 1
            print("Overdraft! $35 fee applied")
            new_balance -=35

        if self.customer.overdraft_count>=2:
            self.customer.is_active =False
            print("Account deactivated due to repeated overdrafts.")
            
        if account_type == "checking":
            self.customer.check = new_balance
            print(f"new checking balance: {self.customer.check}")
            
        else:
            self.customer.save = new_balance
            print(f"new savings balance: {self.customer.save}")
                
        
        self.bank.update_csv(self.customer)
        
    def transfer(self, from_account, to_account, amount, target_customer=None):
        amount = float(amount)
        
        if from_account =="checking":
            if self.customer.check < amount:
                print("Shortage of money")
                return
            self.customer.check -= amount
        elif from_account == "savings":
            if self.customer.save < amount:
                print("Shortage of money")
                return
            self.customer.save -= amount
        else:
            print("Invaild account")
            return
        
        if target_customer is None:
            if to_account == "checking":
                self.customer.check += amount
            elif to_account == "savings":
                self.customer.save += amount
            else: 
                print("Invaild target account")
                return
        else:
            if to_account == "checking":
                target_customer.check += amount
            elif to_account == "savings":
                target_customer.save += amount
            else:
                print("Invaild target account")
        self.bank.update_csv(self.customer)
        if target_customer:
            self.bank.update_csv(target_customer)
        print(f"Transfer successful! New Banlances: checking:{self.customer.check}, savings: {self.customer.save}")
        
            
                
        