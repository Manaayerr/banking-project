import unittest
from banking.bank import Bank
from banking.customer import Customer

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank(csv_file="banking/bank.csv")
        
    def test_load_customers(self):
        self.assertIsInstance(self.bank.customers,dict)
        self.assertIn('10001', self.bank.customers)
        self.assertIsInstance(self.bank.customers['10001'], Customer)
        
    def test_add_customer(self):
        init_count = len(self.bank.customers)
        new_id = str(int(max(self.bank.customers.keys())) + 1)
        
        new_customer = Customer(
            account_id=new_id,
            Fname="Rawan",
            Lname="Magrabi",
            password="Ms1234",
            check=0,
            save=0
            )
        self.bank.customers[new_customer.account_id] = new_customer
        self.assertEqual(len(self.bank.customers), init_count +1)
        
        self.assertIn("10006", self.bank.customers)
        self.assertEqual(self.bank.customers[new_id].Fname,"Rawan")
        self.assertEqual(self.bank.customers[new_id].Lname, "Magrabi")
    
    def test_login_done(self):
        customer = self.bank.login("10003", "uYWE732g4ga1")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.Fname, "melvin")
        
    def test_login_fail(self):
        customer = self.bank.login("10001", "asbcdefg")
        self.assertIsNone(customer)
        
    def test_deposit_checking(self):
        customer = self.bank.login("10003", "uYWE732g4ga1")
        initial_balance = customer.check
        customer.check += 100
        self.assertEqual(customer.check, initial_balance + 100)
        
    def test_deposit_savings(self):
        customer = self.bank.login("10003", "uYWE732g4ga1")
        initial_balance = customer.save
        customer.save += 200
        self.assertEqual(customer.save, initial_balance + 200)
        
    def test_withdraw_checking(self):
        customer = self.bank.login("10003", "uYWE732g4ga1")
        initial_balance = customer.check
        customer.check -= 50
        self.assertEqual(customer.check, initial_balance - 50)
        
    def test_withdraw_savings(self):
        customer = self.bank.login("10003", "uYWE732g4ga1")
        initial_balance = customer.save
        customer.save -= 100
        self.assertEqual(customer.save, initial_balance - 100)
        
if __name__ == "__main__":
    unittest.main()