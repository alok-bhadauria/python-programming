st = input("Enter string : ")
st_2 = ''
for i in st:
    if ('a'<=i<='z') or ('A'<=i<='Z'):
        st_2 += i
print(st_2)
