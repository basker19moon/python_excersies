''' class Encap:
    a = 10
    def display(self):
        print(self.a)

e = Encap()
e.display()
print(e.a)
'''
'''
class Encap:
    __a=10
    def __display(self):
        print(self.__a)
    def show(self):
        self.__display()

e = Encap()
e.show()
'''
class Encap:
    __a=10
    def setA(self, b):
        self.__a = self.__a+b
        
    def getA(self):
        return self.__a

e = Encap()
e.setA(30)
print(e.getA())
