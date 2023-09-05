a = float(input("Enter first side of triangle : "))
b = float(input("Enter second side of triangle : "))
c = float(input("Enter third side of triangle : "))

s = (a+b+c)*1/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Area of triangle : ",area)
