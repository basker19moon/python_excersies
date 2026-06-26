n = int(input("Please Enter Number: "))
arm = n 
f = len(str(n))
sum=0
while n>0:
    r = n%10
    sum = sum+r**f
    n=n//10
if arm == sum:
    print(" Its a Armstrong Number")
else: 
    print("Its not a Armstrong Number")
        