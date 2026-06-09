rows = 5
for i in range(1, rows+1):
    for k in range(rows-i):
        print(" ", end='')
    for j in range(i):
        print('*', end=' ')
    print()