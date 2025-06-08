s=input("Enter a sentence: ")
l1=s.split()
for i in l1:
    if i=="the":
        l1.remove(i)
s=" ".join(l1)
print(s)