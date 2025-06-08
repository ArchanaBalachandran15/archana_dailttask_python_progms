n=int(input("Enter list limit: "))
l1=[]
for i in range(n):
    item=int(input("Enter element:"))
    l1.append(item)
print("List is: ",l1)
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
c=0
for i in range(n):
    if l<=l1[i] and l1[i]<=u:
        c+=1
print("Count of elements between",l,"and",u,"is: ",c)