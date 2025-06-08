s1=input("Enter first string: ")
s2=input("Enter second string: ")

snew1=s2[0:2]+s1[2:]
snew2=s1[0:2]+s2[2:]
r=snew1+" "+snew2
print(r)