# Python progream to sum the given interger
n = int(input('Please Enter the number to do Sum: '))
sum = 0
while n>0:
    r=n%10
    sum = sum+r
    n=n//10
print("Sum of digits of n is : ", sum)