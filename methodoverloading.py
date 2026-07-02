class Mehtodoverloading:   # Methodoverloading in Polymorphism
    def display(self, a = None, b = None, c = None):
        print(a, b, c)

obj = Mehtodoverloading()
obj.display()
obj.display(10)
obj.display(10, 20)
obj.display(10, 20, 30)
