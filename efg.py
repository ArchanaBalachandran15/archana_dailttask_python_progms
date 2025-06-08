from aaa import*
contactbook={"ABC":233567,"XYZ":236897}
def insertion(str)

while True:
    print("Choose Operation from the given list")
    print("1. Insertion")
    print("Exit")
    n=int(input("Enter operation number: "))
    if n==1:
        name=input("Enter name: ")
        insertion(name)
    else:
        exit()