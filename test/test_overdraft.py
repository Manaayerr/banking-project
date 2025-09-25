import unittest
from banking.bank import Bank , Transaction

class TestOverdraft(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.customer = self.bank.login("10003","uYWE732g4ga1")
        self.tran = Transaction(self.customer, self.bank)
        
        