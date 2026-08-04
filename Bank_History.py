transactions = []

while True:

    print("\n       Bank Menu")
    print("1. Deposit")
    print("2. Withdraw")    
    print("3. Current Balance")
    print("4. Transaction History")
    print("5. Largest Deposit")
    print("6. Largest Withdraw")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter the amount you want to deposit: "))
        transactions.append("+"+ str(amount))
        print("Deposited Successfully...")

    elif choice == "2":
        amount = int(input("Enter the amount you want to withdraw: "))
        transactions.append("-"+ str(amount))
        print("Withdraw Successfully...")

    elif choice == "3":
        balance = 0

        for t in transactions:
            if t[0] == "+":
                balance += int(t[1:])
            else:
                balance -= int(t[1:])

        print("Current Balance: ",balance)

    elif choice == "4":
        if transactions == 0:
            print("No Transaction History...")
        else:
            for t in transactions:
                print(t)

    elif choice == "5":
        deposit = []

        for t in transactions:
            if t[0] == "+":
                deposit.append(int(t[1:]))

        if deposit == 0:
            print("No Deposits Done...")
        else:
            print("The Largest Deposit: ", max(deposit))

    elif choice == "6":
        withdraw = []

        for t in transactions:
            if t[0] == "-":
                withdraw.append(int(t[1:]))

        if withdraw == 0:
            print("No Withdraws Done...")
        else:
            print("The Largest Withdraw: ",max(withdraw))

    elif choice == "7":
        print("Thankyou!")
        break

    else:
        print("Invalid choice...")