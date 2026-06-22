'''a = 100
def fun():
    a =10
    print('In fun() a is: ', a)
    fun1()
    fun2()
    print("a is: ", a)

def fun1():
    b = 10
    print('In fun1() b is: ', b)
    print('In fun1() a is: ', a)
    print("a is: ", a)

def fun2():
    global a
    print('Global a is: ', a)
    a = a+1
fun() '''
'''
def display(*n):
    s=0
    for i in n:
        s=s+1
    print(s)
display()
display(1)
display(1,2)
display(2,3,4)
display(1,3,4,5) '''
'''
def hai():
    print('hello!')
    hai()
hai()'''
n=5
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
#print(n)
print(fact(5))
fact(6)