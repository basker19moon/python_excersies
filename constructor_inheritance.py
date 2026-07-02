class Base: 
    def __init__(self, rno, name):
        print("Super class Contrucotr")
        self.rno = rno
        self.name = name
    def dis(self):
        print(self.rno, self.name)

class Derived(Base):
    def __init__(self, rno, name, age):
        super().__init__(rno, name)
        print("Derived Class Contructor")
        self.age = age
    def display(self):
        super().dis()
        print(self.age)
d = Derived(75, "Udvitha", 35)
d.display()
