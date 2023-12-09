st = '1'
n = int(input("Value of N : "))
s = ''
print(st)
while n:
    reg = ''
    for ch in st:
        if ch not in reg:
            count = st.count(ch)
            ft = f'{count}{ch}'
            s += ft
            reg += ch
    print(s)
    n -= 1
    st = s
    s = ''
