s=input("Enter a string: ")
l=len(s)
if l>=3:
    a=s[-3:]
    if a=="ing":
        s1=s.replace("ing","ly")
        print(s1)
    else:
        s1=s+"ing"
        print(s1)
else:
    print(s)