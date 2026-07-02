class Student:
    univ = "xyz"
    def __init__(self, rno, name):
        self.rno = rno
        self.name = name
        Student.univ = 'abc'
        
    def display(self):
        print(self.rno, self.name)
        print(Student.univ)
    
    @staticmethod
    def show():
        Student.univ = 'Kakathiya'
        print(Student.univ)

    @classmethod
    def cmethod(cls):
        cls.univ = 'Oxford'
        print(cls.univ)


s1 = Student(72, "Udvitha Sri")
s1.display()
s2 = Student(73, "Aarush Naitik")
s2.display()
Student.show()
Student.cmethod()
