print("<== SERIES 2 ==>")

x = float(input("Enter value of x : "))
n = int(input("Enter value of n : "))
s = 0
for a in range(n+1):
    if (a%2==0):
        s += x**a
    else:
        s -= x**a
print("Sum of series is : ",s)
