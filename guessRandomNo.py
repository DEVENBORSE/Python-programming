import random

secret_no = random.randint(1,10)

while True:
    guess = int(input("enter the guessed no. of yours from 1 to 9: "))

    if guess == secret_no:
        print("you have successfully guessed the number 🫡")
        break
    
    elif guess < secret_no:
        print("you guessed a little bit low number 😗")
        break
    
    else:
        print("you guessed a little bit higher number 🤷‍♂️")
        break