# Python program to find biggest of 3 number 
a = int(input("Please Enter 1st Number: "))
b = int(input("Please Enter 2nd Number: "))
c = int(input("Please Enter 3rd Number: "))
if a>b and a>c:
    print("a is bigger")
elif b>c:
    print("b is bigger")
else:
    print("c is bigger")
print("EOP")