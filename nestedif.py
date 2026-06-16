# Python program to print biggest of 3 numbers:
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")
print("End of the program")