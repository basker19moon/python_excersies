def is_palindrome(s):
    return s == s[::-1]

string = input("Please Enter a Number: ")
if is_palindrome(string):
    print("Its Palindrome")
else: 
    print("Its Not a Palindrome")

