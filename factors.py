n = int(input("Please Enter a Number: "))
for i in range(1, n+1):
    if (n%i == 0):
        print(i, end=' ')
print("\nprime factors ", end='\n')
for i in range(1, n+1):
    if n%i == 0:
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count = count+1
        if count == 2:
            print(i)
        k=0
        k=i+k
if k == n:
    print(k, "Perfect Number")
else:
    print(k, "Not perfect Number")

sum = 0
for i in range(1, int(n/2)+1):
        
    if n%i==0:
        sum = sum+i
if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")