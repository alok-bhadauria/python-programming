print("<== SERIES 3 ==>")

x = float(input("Enter value of x : "))
n = int(input("Enter value of n : "))
s = 0
for a in range(n+1):
    if a%2==0:
        s += (x**a)/n
    else:
        s -= (x**a)/n
print("Sum of series is : ",s)
