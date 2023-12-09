print("<== FIND THE SMALLEST NUMBER ==>")

a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
c = float(input("Enter third number : "))

if a<b and a<c:
    smallest = a
elif b<a and b<c:
    smallest = b
else:
    smallest = c
print("The smallest number is :",smallest)
