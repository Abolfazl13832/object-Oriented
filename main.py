
class Pride:
    def __init__(self, color, type, speed,rent_money,rental_price):
        self.color = color
        self.type = type 
        self.speed = speed
        super().__init__(rent_money,rental_price)



class Samand:
    def __init__(self, color, type, speed, electric_glass, autopilot,selling_price):
        self.color = color
        self.type = type 
        self.speed = speed
        self.electric_glass = electric_glass
        self.autopilot = autopilot
        super().__init__(selling_price)#با این کار میگیوییم که selling price رو وقتی که از کلاس استفاده کردیم به دومین کلاس پدری ارسال بشه


class Sale:
    def __init__(self , selling_price):
        self.selling_price = selling_price


class Rent:
    def __init__(self , rent_money,rental_price):
        self.rent_money = rent_money
        self.rental_price = rental_price


class SamandSale(Samand,Sale):
    pass
class PrideRent(Pride,Rent):
    pass 

if __name__ == "__main__":
    ss=SamandSale(color="red",type="sangin",speed=220,electric_glass=True,autopilot=False,selling_price=20000)
    pr=PrideRent("yellow","sabok",110,"80M","1M")
    print(SamandSale.mro())
    print(PrideRent.mro())

#در کل اولوت با کلاس سمت چپ یعنی اولین کلاس پدری میباشد 
    