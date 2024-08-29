from models.all_models import Reseller ,Product , Customer


p1 = Product(1,13,140000)
r1 = Reseller("brand #1",'logo #1',p1,'1','2','3','4' )
for i in range(100):
    Customer(1,2,34,5)
print(Customer.con)