n=int(input('Please Enter a Number: '))
rev = 0
while n>0:
    r=n%10  # Here we capture Remainder
    rev=rev*10+r
    n=n//10  # Here we capture quiotent
print("The Reverse of number is: ", rev)