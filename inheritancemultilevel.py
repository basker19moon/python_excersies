class Grandparent:
    def fun1(self):
        print("Function1")

class Parent(Grandparent):
    def fun2(self):
        print("Function2")

class Child(Parent):
    def fun3(self):
        print("Function3")

c = Child()
c.fun3()
c.fun2()
c.fun1()
