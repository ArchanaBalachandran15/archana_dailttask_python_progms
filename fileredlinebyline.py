f=open("mytxtfile2.txt","a")
f.write("welcome")
f.write("good")
f.close()

f=open("mytxtfile2.txt","r")
l1=[]
for i in f:
	l1.append(i.strip())
f.close()
print(l1)