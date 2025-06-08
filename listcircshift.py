n=int(input("Enter limit: "))
l1=[]
l2=[]
for i in range(n):
    ele=int(input("Enter element: "))
    l1.append(ele)
print("list:",l1)
r=int(input("Enter no of rotations: "))
for i in range(-r,n-r):
    l2.append(l1[i])
print("list after shift: ",l2)

