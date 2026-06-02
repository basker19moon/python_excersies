def add(a,b):
    print("*******")
    return a+b
    

#This block only runs when executing math_utils.py directly
if __name__ == "__main__":
    print("Testing the add function directly: ")
    results = add(5,10)
    print(f'5 + 10= {results}')
