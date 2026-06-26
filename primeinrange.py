min = 1
max = 1000
for i in range(min, max+1):
    count=0
    for j in range(1, i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i, end=" ")
    