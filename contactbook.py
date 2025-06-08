contactbook={"ABC":233567,"XYZ":236897}
while True:
    print("Choose Operation from the fillowing list")
    print("1. INSERTION")
    print("2. UPDATION")
    print("3. DELETION")
    print("4. DISPLAY")
    print("5. EXIT")
    n=int(input("Enter operation number: "))
    if n==1:
        name=input("Enter name: ")
        if name in contactbook.keys():
            print("Name",name,"already exist!!")
        else:
            phnno=int(input("Enter number: "))
            contactbook[name]=phnno
            print("SUCCESS")
    elif n==2:
        print("1. Update name")
        print("2. Update number")
        c=int(input("Enter choice: "))
        if c==1:
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
        elif c==2:
            name=input("Enter name: ")
            if name not in contactbook.keys():
                print("Contact",name,"not exist!!")
            else:
                phnno=int(input("Enter new phone number: "))
                contactbook[name]=phnno
                print("Number of",name,"Updated to",phnno,"Successfuly")
        else:
            print("Invalid choice!!")
    elif n==3:
        name=input("Enter name to delete: ")
        if name not in contactbook.keys():
            print("Name",name,"not exist!!")
        else:
            contactbook.pop(name)
            print("Contact",name,"deleted successfuly")
    elif n==4:
        print("Contacts")
        for i,j in contactbook.items():
            print(i," - ",j)
    elif n==5:
        exit()
    else:
        print("Invalid operation!! Choose correct one.")