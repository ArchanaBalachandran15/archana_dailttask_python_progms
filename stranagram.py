str1=input("Enter first string: ")
str2=input("Enter second string: ")
f=0
if len(str1)==len(str2):
    for i in range(len(str1)):
        a=str1[i]
        if str1.count(a)==str2.count(a):
            f=1
        else:
            f=0
if f==1:
    print("Two strings are anagram to each other")
else:
    print("Two strings are not anagram!!")