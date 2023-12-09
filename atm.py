n = int(input("Enter amount to be withdrawn : "))
if n%100 != 0:
    print("Enter a valid amount !")
else:
    w = n-100
    c20 = w//2000
    x = w%2000
    c5 = x//500
    y = x%500
    c2 = y//200
    z = y%200
    c1 = z//100
    c1 = c1 + 1
    print("2000 Notes : ", c20)
    print("500 Notes : ", c5)
    print("200 Notes : ", c2)
    print("100 Notes : ", c1)