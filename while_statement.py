number = 23
running = True

while running: 
    guess =  int(input("Enter  an Integer : "))

    if guess == number:
        print("Congratulation, you guessed it correctly.")
        #this cuases while loop to stop 
        running=False   

    elif guess < number:
        print("No, it is a little higher than that. ")
        #running=False
    else: 
        print('No, it is little lower than that. ')
        #running=False
else:   

    print('while loop is over. ')
    #Do anything else you want to do here
    # 
print('Done')
