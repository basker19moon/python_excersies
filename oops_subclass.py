class SchoolMembers:
    ''' Represent any School Member. '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Intilized School Member: {}'.format(self.name))
    
    def tell(self):
        ''' Tell my details '''
        print('Name :"{}" Age:"{}"'.format(self.name, self.age), end= " ")

class Teacher(SchoolMembers):
    ''' Represents a Teacher'''
    def __init__(self, name, age, salary):
        SchoolMembers.__init__(self, name, age)
        self.salary = salary
        print('Initilzied Teacher: {} '.format(self.name))

    def tell(self):
        SchoolMembers.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMembers):
    ''' Represents a Student. '''
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        print('Initilzied Students: {}'.format(self.name))

    def tell(self):
        SchoolMembers.tell(self)   
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Miss. Udvitha Sri', 40, 100000)
s = Student('Master. Aarush', 5, 100)
print()

members=[t,s]
for member in members:
    # Work for both Teachers and Students
    member.tell()