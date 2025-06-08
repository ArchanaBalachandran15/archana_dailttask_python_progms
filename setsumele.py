set1=set()
for i in range(5):
    item=int(input("Enter element: "))
    set1.add(item)
print("set is: ",set1)
s=0
for i in set1:
    s=s+i
print("Sum of set elements is: ",s)