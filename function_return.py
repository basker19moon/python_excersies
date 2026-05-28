def maximum(x,y):
    if x > y:
        print(x, "is greater")
        return x 
    elif x == y:
        print(x, y, " are equal")
        return "The Numbers are Equal"
    else:
        print(y, " is greator")
        return y
    

print(maximum(100, 7))