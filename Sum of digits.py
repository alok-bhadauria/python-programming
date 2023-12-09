n = int(input("Enter the integer : "))
i=0

while n!=0:
    j=n%10
    i=i+j
    n=n//10
print("Sum of digits : ",i)
