PhoneNumber = input("Enter the number: ")

if len(PhoneNumber) == 10 and PhoneNumber.isdigit() and PhoneNumber[0] in "6789":
    print(f"Phone Number is: {PhoneNumber}")
    print("Valid Phone Number...")

else:
    print("Invalid Phone Number")