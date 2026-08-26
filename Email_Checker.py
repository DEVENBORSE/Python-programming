
# abc@gmail.com

email = input("enter the email address: ")

if email.count("@") == 1:

    at = email.find("@")

    if at > 0 and at < len(email) - 1:
        dot = email.find(".", at)

        if dot != -1 and dot > at+1 and dot < len(email) - 1:
            print("valid email ID")
        else:
            print("Invalid Email ID")
    else:
        print("Invalid Email ID")
else:
    print("Invalid Email ID")




# By regex ( regular expression)

# import re

# email = input("Enter Email: ")

# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# if re.fullmatch(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")