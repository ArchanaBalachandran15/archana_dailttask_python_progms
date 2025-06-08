def addexpense(exp):
    global balance
    if exp in expenses.keys():
        print(exp,"expense already exist")
        amount=int(input("Enter amount: "))
        if balance<amount:
            print("INSUFFICIENT BALANCE!!")
        else:
            expenses[exp]=expenses.pop(exp)+amount
            balance=balance-amount
            print(exp,"expense added")
    else:
        amount=int(input("Enter amount: "))
        if balance<amount:
            print("INSUFFICIENT BALANCE!!")
        else:
            expenses[exp]=amount
            balance=balance-amount
            print(exp,"expense added")
def addbalance(amnt):
    global balance
    balance=balance+amnt
    print("Current balance is: ",balance)
def viewexpense():
    print("EXPENSES ARE: ")
    for i,j in expenses.items():
        print(i," - ",j)
expenses={}
balance=1000
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
        exit()
    else:
        print("INVALID CHOICE!!")