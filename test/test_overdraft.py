import unittest
from banking.bank import Bank , Transaction

class TestOverdraft(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.customer = self.bank.login("10003","uYWE732g4ga1")
        self.tran = Transaction(self.customer, self.bank)
        self.customer.check , self.customer.save = 50.0 , 50.0
        self.customer.overdraft_count = 0
        self.customer.is_active = True
        
    def test_withdraw(self):
        self.tran.withdraw("checking", 50)
        self.assertEqual(self.customer.check , 0.0)
        self.assertTrue(self.customer.is_active)
        
    def test_overdraft(self):
        self.tran.withdraw("checking",100)
        self.assertEqual(self.customer.check, -85.0)
        self.assertEqual(self.customer.overdraft_count,1)
        
    def test_overdraft_limit(self):
        self.tran.withdraw("checking", 200)
        self.assertEqual(self.customer.check, 50.0)
        self.assertFalse(self.customer.is_active)
        
    def test_deactivated_two_overdraft(self):
        self.tran.withdraw("checking",100)
        self.tran.withdraw("checking",100)
        self.assertFalse(self.customer.is_active)
        
    def test_re_activation(self):
        self.customer.is_active = False
        self.customer.check = -80
        self.customer.overdraft_count = 2
        self.bank.reactivate_account(self.customer, 100)
        self.assertTrue(self.customer.is_active)
        self. assertEqual(self.customer.overdraft_count, 0)
        self.assertEqual(self.customer.check,20.0)
        
    
        
if __name__ == "__main__":
    unittest.main() 