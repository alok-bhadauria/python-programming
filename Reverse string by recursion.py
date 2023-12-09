#METHOD 1

str_1 = input("Enter string : ")
str_2 = ''
l = len(str_1)+1

for i in range(1,l):
    x=str_1[-i]
    str_2 += x
print(str_2)

#METHOD 2

str_1 = input("Enter string : ")
print(str_1[::-1])
