print("<== CHECK IF STRING IS PALINDROME OR NOT ==>")

a = input("String to be checked for palindrome or not : ")

if (a == a[::-1]):
    print("This is a palindrome string")
else:
    print("This is not a palindrome string")

print("<== CONVERT CASE OF CHARACTERS IN A STRING ==>")

b = input("String to covert case of characters : ")
UB = b.upper()
LB = b.lower()
SB = b.swapcase()
print("Converted to uppercase : ", UB)
print("Converted to lowercase : ", LB)
print("String with swapped cases : ", SB)
