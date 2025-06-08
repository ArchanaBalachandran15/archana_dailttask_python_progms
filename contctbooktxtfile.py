from functions import*
'''
def filewrite():
    f=open("contacts.txt","w")
    for i,j in contactbook.items():
        a=str(i)+" - "+str(j)+"\n"
        f.write(a)
'''
while True:
    print("Choose Operation from the given list")
    print("1. Insertion")
    print("2. Updation")
    print("3. Deletion")
    print("4. Display")
    print("5. Exit")
    n=int(input("Enter operation number: "))
    if n==1:
        name=input("Enter name: ")
        insert(name)
    elif n==2:
        print("1. Update name")
        print("2. Update number")
        c=int(input("Enter choice: "))
        update(c)
    elif n==3:
        name=input("Enter name to delete: ")
        deletion(name)
    elif n==4:
        display()
    elif n==5:
        filewrite()
        exit()
    else:
        print("Invalid choice!!")