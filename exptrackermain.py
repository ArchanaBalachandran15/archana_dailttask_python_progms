from exptrackerfuns import*
readbalance()
while True:
    print("Choose option from following list")
    print("1. Add Expense")
    print("2. Add Balance")
    print("3. View Expense")
    print("4. Exit")
    c=int(input("Enter option number: "))
    if c==1:
        exp=input("Enter expence name: ")
        addexpense(exp)
    elif c==2:
        amount=int(input("Enter amount to add: "))
        addbalance(amount)
    elif c==3:
        viewexpense()
    elif c==4:
        expwrite()
        exit()
    else:
        print("INVALID CHOICE!!")
        