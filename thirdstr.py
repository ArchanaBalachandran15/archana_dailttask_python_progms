s1=input("Enter first string: ")
s2=input("Enter second string: ")
l1=len(s1)
l2=len(s2)
if l1<=l2:
    n=l1
else:
    n=l2
j=0
k=-1
s3=""
for i in range(0,n,1):
    s3=s3+s1[j]+s2[k]
    j=j+1
    k=k-1
#print(j)
#print(k)
if l1==12:
    print(s3)
elif l1==n:
    s3=s3+s2[:k+1]
    #s3=s3+s2[k::-1]
    print(s3)
else:
    s3=s3+s1[j:]
    print(s3)