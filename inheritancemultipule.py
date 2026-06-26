class Base1:
    def fun1(self):
        print("Function1")

class Base2:
    def fun2(self):
        print("Function2")

class Derived(Base1, Base2):
    def fun3(self):
        print('Function3')

d=Derived()
d.fun3()
d.fun2()
d.fun1()