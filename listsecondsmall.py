n=int(input("list limit: "))
list1=[]
for i in range(n):
    item=int(input("Enter element:"))
    list1.append(item)
print("List is: ",list1)
list1.sort()
print("Second smallest number is",list1[1])
