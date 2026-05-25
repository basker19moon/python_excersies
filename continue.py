while True:
    s=input('Please Enter something: ')
    if s == 'quit' or len(s) < 3:  # Checking length of the string along with quit 
        break
    if len(s) <3:
        print("Too Small")
        continue
    print('Input is of sufficient length')
    #Do other kind of precessing here...
