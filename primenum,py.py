n=int(input("Enter a number: "))
for i in range(1,n):
    if(n%i==0):
        c=c+1
if c>2:
    print("Not a prime")
else:
    print("Prime")