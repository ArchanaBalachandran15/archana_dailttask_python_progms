contactbook={"ABC":233567,"XYZ":236897}
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
def filewrite():
    f=open("contacts.txt","w")
    for i,j in contactbook.items():
        a=str(i)+" - "+str(j)+"\n"
        f.write(a)
