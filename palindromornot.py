n = int(input("Enter a Number: "))
pal = n
rev = 0 
while (n>0):
    r = n%10
    rev = rev*10+r
    n=n//10
if (pal==rev):
    print("Palindrome Number")
else: 
    print("Not a Palindrome Number")
