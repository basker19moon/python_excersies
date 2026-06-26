class Base:
    def fun1(self):
        print("Function1")

class Drived(Base):
    def fun2(self):
        print('Function2')

d=Drived()
d.fun2()
d.fun1()