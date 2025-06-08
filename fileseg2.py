f=open("mytxtfile1.txt","w")
f.write("hsghg\n sgzhggf")
f.close()

f=open("mytxtfile1.txt","r")
d=f.read()
#print(f.read(3))
#print(f.readline())
print(d)
f.close()

'''f=open("mytxtfile1.txt","r")
for i in f:
	print(i)
f.close()'''