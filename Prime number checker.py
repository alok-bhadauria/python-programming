n=int(input("Enter the number : "))
i=1
a=0
while n>=i:
    if n%i==0:
        a+=1
    i+=1
if a == 2:
    print("Prime !")
else:
    print("Not prime !")
