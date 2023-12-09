#METHOD 1 (loop)

str_1 = input("Enter string : ")
check = ''

for i in str_1:
    cnt = 0
    if i not in check:
        for j in str_1:
            if i == j:
                cnt += 1
        print(i,':',cnt)
        check += i

# METHOD 2 (function)

st = input("Enter string : ")
reg = ''
for ch in st:
    if ch not in reg:
        count = st.count(ch)
        print(f'{ch} : {count}')
        reg += ch
