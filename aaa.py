from efg import contactbook
def insertion(name):
    if name in contactbook.keys():
        print("Name",name,"already exist!!")
    else:
        phnno=int(input("Enter number: "))
        contactbook[name]=phnno
        print("Contact",name,"inserted successfuly")

