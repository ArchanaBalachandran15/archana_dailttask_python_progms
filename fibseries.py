n=int(input("Enter a limit: "))
i=0
a=-1
b=1
c=0
while(i<n):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
    i+=1

