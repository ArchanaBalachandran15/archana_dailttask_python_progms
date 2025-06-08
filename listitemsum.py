n=int(input("Enter a limit: "))
l1=[]
for i in range(n):
    item=int(input("Enter:"))
    l1.append(item)
print("list is: ",l1)
s=0
for i in l1:
    s+=i
print("Sum of list elements is: ",s)