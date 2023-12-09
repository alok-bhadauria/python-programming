cart=[]
a = 0
while a == 0:
    x = input("Enter new item : ")
    if x == "":
        a=1
        print("No new item regiestered")
        print("Your cart is ready for check-out")
        break
    else:
        cart.append(x)
print("Your cart : ",cart)
