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
    
    def test_transfer_checking_to_savings(self):
        init_check = self.cus1.check
        init_save = self.cus1.save
        self.tran1.transfer("checking","savings", 200)
        self.assertEqual(self.cus1.check, init_check -200)
        self.assertEqual(self.cus1.save, init_save +200)
        
    def test_transfer_savings_to_checking(self):
        init_check =self.cus1.check
        init_save = self.cus1.save
        self.tran1.transfer("savings", "checking", 100)
        self.assertEqual(self.cus1.save, init_save - 100)
        self.assertEqual(self.cus1.check, init_check +100)
        
    def test_transfer_to_other_customer(self):
        init_check_1 = self.cus1.check
        init_check_2 = self.cus2.check
        self.tran1.transfer("checking","checking",300,target_customer=self.cus2)
        self.assertEqual(self.cus1.check, init_check_1 -300)
        self.assertEqual(self.cus2.check,init_check_2 +300)
    def test_transfer_overTheLimit(self):
        init_check = self.cus1.check
        self.tran1.transfer("checking","savings" , 5000)
        self.assertEqual(self.cus1.check, init_check)
        
        
        
if __name__ == "__main__":
    unittest.main()
        
        