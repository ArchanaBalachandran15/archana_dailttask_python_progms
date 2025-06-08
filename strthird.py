s1=input("Enter first string: ")
s2=input("Enter second string: ")
s3=s1[0]+s2[-1]+s1[1]+s2[-2]+s1[2:]+s2[:-2]
print(s3)
