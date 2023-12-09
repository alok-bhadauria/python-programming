n = int(input("Enter a number : "))

a=1
s=0

while a <= n:
    if a%2==0:
        s+=a
    a+=1

print("Sum of even numbers upto",n,"is",s)
