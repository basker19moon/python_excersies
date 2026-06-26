class Base:
    def fun1(self):
        print("Function1")

class Derived1(Base):
    def fun2(self):
        print("Function2")

class Derived2(Base):
    def fun3(self):
        print('Function3')

d1=Derived1()
d1.fun2()
d1.fun1()

d2 = Derived2()
d2.fun3()
d2.fun1()
