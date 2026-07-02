class Number:                               # Polymorphism Operator overloading
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        ret = Number(a, b, c)
        return ret
    def __lt__(self, other):
        o1 = self.a + self.b + self.c
        o2 = other.a + other.b + other.c
        if (o1<o2):
            return True
        else: 
            return False

n1 = Number(1, 2 , 3)
n2 = Number(4, 5, 6)
n3 = n1+n2
print(n3.a, n3.b, n3.c)
print(n1<n2)
