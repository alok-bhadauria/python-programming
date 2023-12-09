print("<== DETERMINE PRIME OR COMPOSITE NUMBER ==>")

a=int(input("Enter a number : "))
c=0
if a==0:
    print("The number is neither prime nor composite.")

for i in range(1,a+1):
    rem = a%i
    if (rem == 0):
        c = c+1

if (c == 1):
    print("The number is neither prime nor composite.")
        
if(c == 2):
    print("The number is a prime number.")

elif(c >= 3):
    print("The number is a composite number.")
