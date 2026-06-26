class Student:
    def __init__(self, rno, name):
        self.rno = rno
        self.name  = name
    
    #def __init__(self):
    #    print("Zero Constructor")
    
    def display(self):
        print("Rno is: ", self.rno)
        print('Name is: ', self.name)

s1=Student(10, "Udvitha")
print("S1 Object info: ")
s1.display()

s2=Student(20, "Aarush")
print("S2 Object info: ")
s2.display()

s3=Student(30, 'Krishna')
print("S3 Object info: ")
s3.display()