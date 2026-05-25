#Printing Uppercase (A to Z ) to lowercase (a-z) using for loop

print("Alphabet A-Z:", end=" ")
for i in range(65, 91):  # ASCII value of A is 65 and Z is 90
    print(chr(i), end=" ")

print("\n\nAlphabet a-z:", end=" ")
for i in range(97, 123): # ASCII value of a is 97 and z is 122
    print(chr(i), end=" ")
