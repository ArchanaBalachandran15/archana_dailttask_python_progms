expenses={}
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
def expwrite():
    f=open("expenselist.txt","w")
    for i,j in expenses.items():
        a=str(i)+" - "+str(j)+"\n"
        f.write(a)
    f.close()
def readbalance():
    global balance
    f=open("balance.txt","r")
    d=(f.read()).strip()
    l1=d.split()
    for i in l1:
        if "=" in i:
            l1.extend(i.split("="))
    for j in l1:
        if j.isdigit():
            balance=int(i)
            print("Initial balance is: ",balance)
    f.close()