def sumlist(l1):
    s=0
    for i in l1:
        s+=i
    return s
list1=[]
n=int(input("Enter limit: "))
for i in range(n):
    i=int(input("Enter element: "))
    list1.append(i)
print("list is: ",list1)
result=sumlist(list1)
print("Sum of elements is: ",result)