print("DETERMINE A PALINDROME, AN ARMSTRONG OR A PERFECT NUMBER")
def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev =  rev * 10 + dig
        n = n//10
    if temp == rev:
        print(temp,"is a palindrome")
    else:
        print(temp,"is not a palindrome")
def armstrong(n):
    count = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        count += digit ** 3
        temp //= 10
    if n == count:
        print(n,"is an armstrong number")
    else:
        print(n,"is not an armstrong number")
def perfect(n):
    count = 0
    for i in range(1,n):
        if n % i == 0:
            count = count + i
    if count == n:
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
if __name__ == '__main__':
    n=int(input("Enter the number : "))
    palindrome(n)
    armstrong(n)
    perfect(n)
