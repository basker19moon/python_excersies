class Pattern:
    def __init__(self):
        self.rows=5
        self.name="*"

    def print_pattern(self):
        for i in range(1, self.rows+1):
            for k in range(self.rows-i):
                print(" ", end="")
            for j in range(i):
                print(self.name, end=" ")
            print()

p1=Pattern()
p1.rows=8
p1.name="&"
p1.print_pattern()
p2=Pattern()
p2.rows=10 
p2.name="+"
p2.print_pattern()
p3=Pattern()
p3.print_pattern()
