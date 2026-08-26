

# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# print("thankyou")




# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except ValueError as v:
#     print("Heyyyy")
#     print(v)

# except Exception as e:
#     print(e)

# print("thankyou")




# # raising exception

# a = int(input("enter the value of a: "))
# b= int(input("enter the value of b: "))

# if(b==0):
#     raise ZeroDivisionError("hey our program is not meant to divide number by zero")
# else:
#     print(f"the division a/b is {a/b}")





# try-Finally

def main():

    try:
        a=int(input("hey, enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("hey i am inside of finally")

main()