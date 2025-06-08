import mysql.connector

myexpdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='db1')

expcursor=myexpdb.cursor()
#expcursor.execute("CREATE TABLE balance (balamount int)")
#expcursor.execute("CREATE TABLE expenses (expense varchar(10), amount int)")
#expcursor.execute("INSERT INTO balance (balamount) values(1000)")
#myexpdb.commit()

while True:
    print("Choose option from the following list")
    print("1. Add expense")
    print("2. Add balance")
    print("3. View expenses")
    print("4. Exit")
    c=int(input("Enter choice: "))
    if c==1:
        expcursor.execute("SELECT expense FROM expenses")
        explist=expcursor.fetchall()
        exp=input("Enter expense: ")
        f=0
        for i in range(len(explist)):
            if exp==explist[i][0]:
                f=1
                break
        if f==1:
            print("Expense already exist.")
            newamount=int(input("Enter amount: "))
            expcursor.execute("SELECT balamount FROM balance")
            balancelist=expcursor.fetchall()
            if newamount<balancelist[0][0]:
                expcursor.execute("SELECT amount FROM expenses WHERE expense=%s",(exp,))
                oldamount=expcursor.fetchall()
                totalamount=oldamount[0][0]+newamount
                newbalance=balancelist[0][0]-newamount
                expcursor.execute("UPDATE expenses SET amount=%s WHERE expense=%s",(totalamount,exp))
                expcursor.execute("UPDATE balance SET balamount=%s",(newbalance,))
                myexpdb.commit()
                print(exp," expense added")
            else:
                print("Insufficient Balance!!!")
        else:
            amnt=int(input("Enter amount: "))
            expcursor.execute("SELECT balamount FROM balance")
            balancelist=expcursor.fetchall()
            if amnt<balancelist[0][0]:
                newbalance=balancelist[0][0]-amnt
                expcursor.execute("INSERT INTO expenses(expense, amount) values(%s,%s)",(exp,amnt))
                expcursor.execute("UPDATE balance SET balamount=%s",(newbalance,))
                myexpdb.commit()
                print(exp," expense added")
            else:
                print("Insufficeint balance")
    elif c==2:
        expcursor.execute("SELECT balamount FROM balance")
        balancelist=expcursor.fetchall()
        amnt=int(input("Enter amonut to add: "))
        newbalance=balancelist[0][0]+amnt
        expcursor.execute("UPDATE balance SET balamount=%s",(newbalance,))
        myexpdb.commit()
        print("Balance amount added. New balance is ",newbalance)
    elif c==3:
        print("Expenses")
        expcursor.execute("SELECT * FROM expenses")
        l1=expcursor.fetchall()
        for i in range(len(l1)):
            print(l1[i][0]," - ",l1[i][1])
    elif c==4:
        exit()
    else:
        print("Invalid Choice!!")
