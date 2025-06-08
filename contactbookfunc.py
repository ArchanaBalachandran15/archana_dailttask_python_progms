def insert(name):
    if name in contactbook.keys():
        print("Name",name,"already exist!!")
    else:
        phnno=int(input("Enter number: "))
        contactbook[name]=phnno
        print("Contact",name,"inserted successfuly")
def update(choice):
    if choice==1:
        oldname=input("Enter old name: ")
        if oldname not in contactbook.keys():
            print("Name",oldname,"Not exist!!")
        else:
            newname=input("Enter new name: ")
            if newname in contactbook.keys():
                print("Name",newname,"already exist")
            else:
                contactbook[newname]=contactbook.pop(oldname)
                print("Name",oldname,"Updated to",newname,"Successfuly")
    elif choice==2:
        name=input("Enter name: ")
        if name not in contactbook.keys():
            print("Contact",name,"not exist!!")
        else:
            phnno=int(input("Enter new phone number: "))
            contactbook[name]=phnno
            print("Number of",name,"Updated to",phnno,"Successfuly")
    else:
        print("Invalid choice!!")
def deletion(name):
    if name not in contactbook.keys():
        print("Name",name,"not exist!!")
    else:
        contactbook.pop(name)
        print("Contact",name,"deleted successfuly")
def display():
    print("Contacts")
    for i,j in contactbook.items():
        print(i," - ",j)
contactbook={"ABC":233567,"XYZ":236897}
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
        exit()
    else:
        print("Invalid choice!!")