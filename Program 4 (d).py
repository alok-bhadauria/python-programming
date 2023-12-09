print("<== SERIES 4 ==>")

x = float(input("Enter value of x : "))
n = int(input("Enter value of n : "))
s = 0
a = 1
factorial = 1
for a in range (1,n+1):
    factorial = factorial*a
    if a%2==0:
        s += (x**a)/factorial
    else:
        s -= (x**a)/factorial
print("Sum of series is : ",s)
