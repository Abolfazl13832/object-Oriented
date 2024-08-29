class User:

    def __init__(self,username,password,fullname,email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
    
    def check_password(self,password):
        return self.password == password
    



class Customer (User):
    counter = 0   #class attrs

    def __init__(self,username,password,fullname,email):
        self.wallet_amount = 0 
        self.is_enable = False
        
        Customer.counter+=1
        super().__init__(username,password,fullname,email)

    @staticmethod
    def singup(username,password,fullname,email):
        if len(str(password)) <=5:
            print("try again")
            return None
        else:
            print("success")
            c1 = Customer(username,password,fullname,email)
            return c1

        
        
        

    def __str__(self):
        return self.username
    def check_password(self,password):
        return self.password == password

    def set_enable(self):
        self.enable = True


