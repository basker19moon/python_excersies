# Python progream to find the factorial of the give number:
n = int(input("Please Enter number: "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("Factorial of ", n, 'is ', fact)