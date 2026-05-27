x = 50

def function_local(x):
    print(" x is ", x)

    x =2
    print("changed local x to ", x)

function_local(x)
print("x is still ", x )
