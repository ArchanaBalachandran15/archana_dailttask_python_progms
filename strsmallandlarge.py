s=input("Enter a sentence: ")
l1=s.split(" ")
print(l1)
l2=[]
for i in l1:
    l2.append(len(i))
    l2.sort()
    if len(i)==l2[0]:
        small=i
    elif len(i)==l2[-1]:
        large=i
print("Small word is: ",small)
print("Large word is: ",large)