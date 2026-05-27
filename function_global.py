#function with global variable
x = 50 

def function_global():
    global x 
    print("x is ", x)
    x = 2
    print("changed global x to ", x)

function_global()
print("value of x is ", x)