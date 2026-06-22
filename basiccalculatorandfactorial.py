# Simple calculator:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Sum: ", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)
print("Quotient: ", a/b)

# Factorial of a number!
def factorial(n):
    if n==0:
        return 1
    else: 
        return n * factorial(n-1)

num=int(input("Please a Enter a number: "))
print("Factorial: ", factorial(num)) 