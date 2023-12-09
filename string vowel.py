a = input("Enter string : ")

# remove vowels
b = "aeiouAEIOU"
c = ""
for i in a:
    if i not in b:
        c += i
print(c)

#remove capital letters
b = ""
for i in a:
    if not ("A" <= i <= "Z"):
        b += i
print(b)

#remove small letters
b = ""
for i in a:
    if not ("a" <= i <= "z"):
        b += i
print(b)

#count letters
b = 0
for i in a:
    if ("a"<=i<="z") or ("A"<=i<="Z"):
        b+=1
print(b)

#remove special characters
b = ""
for i in a:
    if ("a"<=i<="z") or ("A"<=i<="Z") or ("0"<=i<="9") or (i==" "):
        b+=i
print(b)

#count and display words ending with letter e or E
a = a.split()
b = 0
c = ""
for i in a:
    if i[-1] == 'e' or i[-1] == 'E':
        b += 1
        c += i
        c += " "
print("No. of words ending with e/E : ",b)
print(c)
