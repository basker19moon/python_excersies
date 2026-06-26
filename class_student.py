class student:
    rno = 10
    name = "Udvitha"
    def display(self):
        rno=100 #local variable
        print(rno)
        print('Roll No is: ', self.rno)
        print('Name is: ', self.name)

s1=student()
s1.display()
s2=student()
s2.rno=20
s2.name = "Aarush"
s2.display()

