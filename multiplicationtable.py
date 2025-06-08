n=int(input("Enter a number: "))
print("MULTIPLICATION TABLE OF NUMBER",n)
p=0
for i in range(1,16):
    p=i*n
    print(i," x ",n,"=",p)
