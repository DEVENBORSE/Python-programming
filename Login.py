user = "Deven"
pwd = 1234

attempt = 0

while attempt < 3:
    username = input("Enter the username: ")
    password = int(input("Enter the password: "))

    if username == user and pwd == password:
        print("Login Successful...")
        print("Welcome Admin...")
        break
    else:
        attempt += 1

        if attempt<3:
            print("Invalid Username and password...")
            print(f"The remaining attempt are {3-attempt}")
        else:
            print("Account Locked")
            print("Contact Administrator")