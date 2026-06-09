name = input("Please Enter the patter to print: ")
rows = 5
for i in range(1, rows+1):
    for k in range(rows-i):
        print(' ', end='')
    for j in range(i):
        print(name, end=' ')
    print()
