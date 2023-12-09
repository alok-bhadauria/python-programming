n= int(input("Enter integer : "))     
i=1
fact=1
if n == 0:
    print("Factorial is : 1")
else:
    while i<=n:
        fact=fact*i
        i+=1
    print("Factorial is : ",fact)
