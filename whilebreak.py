i = 1 
while i <=10:
    print(i)
    if i==5:
        break
    i = i+1
print('For Loop')
for i in range(1, 11, 1):
    if i==5:
        continue
    print(i)


a=[10, 2.5, "abc"]
for i in a:
    print(i)

print('sum of n natural number')

i=1 
n=int(input("please enter number: ")) 
a=0
while i<=n:
    a=a+i
    i=i+1

print('sum of n natural number: ', a)