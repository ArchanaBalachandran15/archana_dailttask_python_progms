n=int(input("Enter list limit: "))
list1=[]
for i in range(n):
    item=input("Enter string: ")
    list1.append(item)
print(list1)
c=0
for i in list1:
    if len(i)>=2:
        if i[0]==i[-1]:
            c+=1
print("no.of strings with length is 2 or more and string starts and ends with same chaaracter is: ")
print(c)


