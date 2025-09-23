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
        
if __name__ == "__main__":
    unittest.main()