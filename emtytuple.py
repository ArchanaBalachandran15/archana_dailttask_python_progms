list1=[]
n=int(input("List limit: "))
for i in range(n):
    print("Enter",i,"th tuple limit")
    m=int(input())
    print("Enter",i,"th tuple elements")
    l1=[]
    for j in range(m):
        item=input()
        l1.append(item)
    list1.append(tuple(l1))
print("List of tuples is: ",list1)
list2=[]
for i in list1:
    if len(i)>0:
        list2.append(i)
print("List of tuples after removing empty tuples:")
print(list2)