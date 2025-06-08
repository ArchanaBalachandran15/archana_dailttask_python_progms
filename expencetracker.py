initialbalance=1000
expense={}
while True:
    print("Choose option from following list")
    print("1. ADD EXPENSE")
    print("2. ADD BALANCE")
    print("3. VIEW EXPENSE")
    print("4. EXIT")
    op=int(input("Enter option number: "))
    if op==1:
        exp=input("Enter expense name: ")
        if exp in expense.keys():
            print(exp,"expense already exist.")
            amnt=int(input("Enter amount: "))
            if initialbalance<amnt:
                print("Insufficient balance!!")
            else:
                expense[exp]=expense.pop(exp)+amnt
                initialbalance=initialbalance-amnt
                print(exp,"expense added.")
        else:
            amnt=int(input("Enter amount: "))
            if initialbalance<amnt:
                print("Insufficient balance!!")
            else:
                expense[exp]=amnt
                initialbalance=initialbalance-amnt
                print(exp,"expense added.")
    elif op==2:
        newamnt=int(input("Enter amount to add: "))
        initialbalance=initialbalance+newamnt
        print("New balance is: ",initialbalance)
    elif op==3:
        print("Expenses are")
        for i,j in expense.items():
            print(i," - ",j)
    elif op==4:
        exit()
    else:
        print("Invalid option!!")