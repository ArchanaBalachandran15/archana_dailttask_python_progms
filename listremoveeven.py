n=int(input("Enter list limit: "))
list1=[]
for i in range(n):
    item=int(input("Enter element:"))
    list1.append(item)
print("List is: ",list1)
list2=[]
for i in list1:
    if i%2!=0:
        list2.append(i)
print("List after removing even numbers")
print(list2)
