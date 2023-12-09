import time

a = 'Password'
c = 3

while True:
    b=input("Enter password : ")

    if a == b:
        print("Correct Password !")
        break

    else:
        c-=1
        print("Incorrect Password, ",c,"attempts left !","wait for 5 seconds to try again.")
        time.sleep(.5)
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)

