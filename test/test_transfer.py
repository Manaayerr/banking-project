import unittest
from banking.bank import Bank
from banking.customer import Customer
from banking.bank import Transaction

class TestBankTransfer(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.cus1=Customer("20001","Lili","smith", "pass1",check=1000,save=500)
        self.cus2=Customer("20002","sachi","benz", "pass2",check=500,save=1000)
        self.bank.customers[self.cus1.account_id] = self.cus1
        self.bank.customers[self.cus2.account_id] = self.cus2
        self.tran1 = Transaction(self.cus1, self.bank)