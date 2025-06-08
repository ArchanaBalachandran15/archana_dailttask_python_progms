n=int(input("Enter list limit: "))
list1=[]
for i in range(n):
    item=int(input("Enter element:"))
    list1.append(item)
print("List is: ",list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i]==list1[j]:
            list1[j]=" "
list2=[]
for i in list1:
    if i!=" ":
        list2.append(i)
print("List after removing duplicate values: ")
print(list2)

