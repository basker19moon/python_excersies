n = int(input("Enter a Number: "))
strong = n
f = 0
sum = 0
while (n>0):
    r = n%10
    f = 1
    for i in range(1, r+1):
        f = f*i
    sum = sum+f
    n= n//10

if strong == sum:

    print("Strong Number")
else:
    print("Not Strong Number")


