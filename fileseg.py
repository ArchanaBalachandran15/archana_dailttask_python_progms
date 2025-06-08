f=open("mytxtfile.txt","x")
f.write("hello good morning")
f.close()

f=open("mytxtfile.txt","r")
d=f.read()
print(d)
f.close()
