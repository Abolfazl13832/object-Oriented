class A:
    def greeting(self):
        print("hello from A")
class B:
    # def greeting(self):
    #     print("hello from B")
    pass
class C(B):
    # def greeting(self):
    #     print("hello from C")
    pass
class D(B,A):
    # def greeting(self):
    #     print("hello from D")
    pass
class E(D,C):
    # def greeting(self):
    #     print("hello from E")
    pass


if __name__ == "__main__":
    e=E()
    print(E.mro())
    e.greeting()

#یک نمونه از ساختار درختی ارثبری چند گانه است بهترین کار این که این ساختار درختی رو یاد بگیریم

