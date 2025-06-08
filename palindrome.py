n=int(input("Enter a number: "))
a=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if a==rev:
    print("Palindrome")
else:
    print("Not a palindrome!!")
