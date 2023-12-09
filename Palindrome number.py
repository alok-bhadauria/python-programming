n=int(input("Enter number : "))
i=0
j=0
check=n
while n!= 0:
    j = n%10
    i = i*10+j
    n=n//10
if check==i:
    print("Palindrome !")
else:
    print("Not a palindrome !")
