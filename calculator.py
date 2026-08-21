class calculator:
    num1 = int(input("enter the 1st number: "))
    num2 = int(input("enter the 2nd number: "))

    choice = int(input("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Exit \nEnter your choice: "))

    if choice == 1:
        print(f"{num1} + {num2} = {num1+num2} ")
    
    elif choice == 1:
        print(f"{num1} + {num2} = {num1+num2} ")
    elif choice == 2:
        print(f"{num1} - {num2} = {num1-num2} ")
    elif choice == 3:
        print(f"{num1} * {num2} = {num1*num2} ")
    elif choice == 4:
        print(f"{num1} / {num2} = {num1/num2} ")
    elif choice == 5:
        print("thankyou")
    else:
        print("invalid input")