class Student:
    rno = 10
    name = 'Ramesh'
    def display(self):
        rno = 100
        print(rno)
        print('Roll NO is ', self.rno)
        print('Name is ', self.name)

s1=Student()
s1.display()
s2=Student
s2.rno=200
s2.name='Bhaskar'
s2.display(s2)
