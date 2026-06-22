n = int(input("Please Enter a Number: "))
count = 0
for i in range(1, n+1):
    if n%i==0:
        count = count+1

if count==2:
    print("\n",n, "is Prime Number")
else: 
    print('\n',n, " is not Prime Number")
#=======================================================
flat = 0
for i in range(2, int(n/2)+1):
    if n%i==0:
        flag = 0 
        break
print("\nSecond Logic")
if flag == 0:
    print("\n", n, "Not Prime")
else:
    print("\n", n, "Prime")