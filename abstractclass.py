from abc import ABC, abstractmethod

class AbstractClassDemo1(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def show(self):
        pass

class AbstractClassDemo2(AbstractClassDemo1):  #Abstract Class

    def display(self):
        print("AbstractClassDemo2 display()")

class AbstractClassDemo3(AbstractClassDemo1):  #Concrete Class

    def display(self):
        print('AbstractClassDemo3 display()')
    def show(self):
        print("AbstractClassDemo3 show()")


obj = AbstractClassDemo3()
obj.display()
obj.show()