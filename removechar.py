a=input("Enter string: ")
s=""
for i in a:
    if i.isdigit():
        s=s+i
print("String after removing all characters: ",s)