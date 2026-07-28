# ===== ATM MENU =====
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# Enter your choice: 1

# Current Balance: ₹5000.00



def show_choices():
    print("-" * 32)
    print("     Welcome to ATM Machine")
    print("-" * 32)

    print("1. Balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

def check_Balance(balance):
    print(f"\nCurrent Balance: ₹{balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount you want to deposit: "))

    if amount > 0:
        balance += amount
        print(f"The amount : {amount:.2f} is deposited...")
    else:
        print("Invalid Input...")

    return balance

def withdraw(balance):
    amount = float(input("enter the amount you want to withdraw: "))

    if amount<=0:
        print("Invalid amount!...")
    elif amount > balance:
        print("Insufficient balance...")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")

    return balance

def main():
    balance = 5000.0

    while True:
        show_choices()
        choice = input("Enter your choice: ")

        if choice == "1":
            check_Balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thankyou for visiting ATM machine")
            break
        else:
            print("Invalid Input")

main()
    