n=int(input("Enter a number: "))
a=n
s=0
while(n>0):
    d=n%10
    p=d**3
    s=s+p
    n=n//10
if s==a:
    print("Armstrong number")
else: 
    print("Not armstrong")