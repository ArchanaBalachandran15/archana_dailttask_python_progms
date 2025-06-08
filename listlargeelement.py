n=int(input("Enter a limit: "))
list1=[]
for i in range(n):
    ele=int(input("Enter:"))
    list1.append(ele)
print("list is: ",list1)
large=0
for i in list1:
    if i>large:
        large=i
print("Largest elements is: ",large)