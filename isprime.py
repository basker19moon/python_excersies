# Python programm to find the given number is prime or not!
def is_prime(n):
    if n<=1:
        return False
    else: 
        for i in range(2, n):
            if n%i ==0:
                return False
            else:
                return True

num = int(input("Please Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")