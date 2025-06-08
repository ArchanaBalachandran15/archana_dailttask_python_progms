s=input("Enter a sentence: ")
l1=s.split(" ")
s=l=l1[0]
print(l1)
for i in l1:
    if len(i)<len(s):
        s=i
    if len(i)>len(l):
        l=i
print("Small word is: ",s)
print("Large word is: ",l)