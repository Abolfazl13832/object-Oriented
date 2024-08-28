class User:
    def __init__(self,username,password,fullname,email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
    
    def check_password(self,password):
        return self.password == password



class Customer:
    counter = 0   #class attrs

    def __init__(self,username,password,fullname,email):
        self.wallet_amount = 0 
        self.is_enable = False
        super().__init__(username,password,fullname,email)


    def __str__(self):
        return self.username

    def check_password(self,password):
        return self.password == password
    
    def set_enable(self):
        self.enable = True


class Reseller(User):
    def __init__(self, brand,logo,*args,**kwargs):
        self.brand = brand
        self.logo = logo
        super().__init__(*args, **kwargs)

    def __str__(self) :
        return self.username

