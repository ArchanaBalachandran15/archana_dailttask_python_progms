n=int(input("Enter list limit: "))
l1=[]
for i in range(n):
    ele=input("Enter element: ")
    l1.append(ele)
print("list is: ",l1)
l2=[]
t=(0,4,5)
for i in range(n):
    if i not in t:
        l2.append(l1[i])
print("List after removing 0th, 4th and 5th elements: ")
print(l2)