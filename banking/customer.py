class Customer:
    def __init__(self, account_id, Fname, Lname, password, check, save):
        self.account_id = account_id
        self.Fname = Fname
        self.Lname = Lname
        self.password = password
        self.check = float(check)
        self.save = float(save)
        
    def __str__(self):
        return f"{self.account_id}: {self.Fname} {self.Lname} - check: {self.check} save: {self.save} "