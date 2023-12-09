print("<== FIND THE LARGER OF TWO NUMBERS ==>")

a = float(input("Enter first number : "))
b = float(input("Enter second number : "))

if a>b:
    print(a,"is greater than",b)
elif b>a:
    print(b,"is greater than",a)
else:
    print("Both numbers are equal.")
