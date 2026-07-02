class Base:       #Method overriding in Polymorphism
    def display(self):
        print("Base Class display()")
class Derived(Base):
    def display(self):
        print("Derived Class display()")
        #return super().display()
obj = Derived()
obj.display()