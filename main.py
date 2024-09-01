from abc import ABC ,abstractmethod
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


class Rent(ABC):
    def __init__(self , rent_money,rental_price):
        self.rent_money = rent_money
        self.rental_price = rental_price

    @abstractmethod
    def show_banner(self):
        """ابسترکت متود یعنی این که اون کلاسی که از rent  .استفاده میکنه باید این متود رو داشته باشه وگرنه اون ارثبری مورد قبول نیست."""
        pass


class SamandSale(Samand,Sale):
    pass
class PrideRent(Pride,Rent):
    def show_banner(self):
        return f"show banner"

if __name__ == "__main__":
    ss=SamandSale(color="red",type="sangin",speed=220,electric_glass=True,autopilot=False,selling_price=20000)
    pr=PrideRent("yellow","sabok",110,"80M","1M")#اینم خطا داده بود چون متود show_banner رو نداشت بعد این که ساختم درست کار کرد
    # r=Rent(3,3)#الان این خطا داد
    print(pr)

    """
    در زبان برنامه‌نویسی پایتون، کلاس‌ها می‌توانند به صورت abstract تعریف شوند. یک کلاس abstract به معنی یک کلاس است که نمی‌تواند مستقیماً ایجاد شود و تنها می‌تواند توسط کلاس‌های فرزند ارث بری شود. این کلاس‌ها برای تعریف یک الگوی کلی برای کلاس‌های فرزند استفاده می‌شوند و نمی‌توانند مثال ایجاد کنند.
    """