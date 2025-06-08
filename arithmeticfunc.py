def add(a,b):
    s=a+b
    return s
def sub(a,b):
    return a-b
def mul(a,b):
    p=a*b
    print("product is:",p)
def div(a,b):
    d=a/b
    return d
while True:
    print("Choose oprations from the given list")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT")
    n=int(input("Enter option: "))
    if n==1:
        i=int(input("Enter values to add: "))
        j=int(input())
        s=add(i,j)
        print("Sum is: ",s)
    elif n==2:
        i=int(input("Enter values to subtract: "))
        j=int(input())
        d=sub(i,j)
        print("Diffrence is:",d)
    elif n==3:
        i=int(input("Enter values to multiply: "))
        j=int(input())
        mul(i,j)
    elif n==4:
        i=int(input("Enter values to divide: "))
        j=int(input())
        d=div(i,j)
        print("Result is",d)
    elif n==5:
        exit()
    else:
        print("Invalid option")