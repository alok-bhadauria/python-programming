print("<== FIND LCM AND HCF (GCD) OF TWO INTEGERS==>")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
HCF = 1

for i in range(2, a+1):
    if(a%i == 0 and b%i == 0):
        HCF = i

LCM = (a*b)/HCF

print("For",a,"and",b,"\n LCM is : ",LCM,"\n HCF is : ",HCF)
