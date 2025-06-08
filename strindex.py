s=input("Enter a string: ")
pos=int(input("Enter index value: "))
t1=s[:pos]+s[pos+1:]
print("string after removing ",pos,"th index character is: ",t1)
