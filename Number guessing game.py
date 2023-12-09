import random

b = random.randrange(1,101)

while True:
    a = int(input("Guess a number (1-100): "))
    
    if a == b:
        print("Congrats, You guessed it right !")
        break
    elif a < b:
        if (a+10)<b:
            print("Too small, Try again !")
        else:
            print("Small, Try again !")
    elif a > b:
        if (a-10)>b:
            print("Too large, try again !")
        else:
            print("Large, Try again !")
    elif a == b:
        break
