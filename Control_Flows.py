number = 23

guess=int(input("Please Enter an Interger: "))

if guess == number:
    print("congratulation, you gussed it. ")
    print('but you do not win any prize')
elif guess < number:
    print("No, it is little higher than that")
else:
    print("No, it is a little lower than that")

print("Done")