n=int(input("Enter a number: "))
if n%3==0:
    if n%5==0:
        print(n,"is divisible by both 3 and 5")
    else:
        print(n,"is not divisible by both 3 and 5")
else:
    print(n,"is not divisible by both 3 and 5")