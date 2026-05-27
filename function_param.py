def print_max(a, b):
    if a > b:
        print(a, " is the max ")
    elif a == b:
        print(a, " is equal to ", b)
    else:
        print(b, "is greater")


#directly pass the literal values
print_max(8, 10)
print_max(10, 10)
print_max(120, 500)
x=236
y=698
print_max(x,y)
print_max(y,x)