# Press Ctrl + c
try:
    text = input('Please Enter somthing: --> ')
except EOFError:
    print("Why did you do an EOF on me? ")
except KeyboardInterrupt:
    print('You cancelled the Operation. ')
else:
    print("You Entered {}".format(text))
