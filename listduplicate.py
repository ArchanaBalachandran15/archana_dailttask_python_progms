n=int(input("Enter list limit: "))
list1=[]
for i in range(n):
    item=int(input("Enter element:"))
    list1.append(item)
print("List is: ",list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("List after removing duplicates:")
print(list2)


