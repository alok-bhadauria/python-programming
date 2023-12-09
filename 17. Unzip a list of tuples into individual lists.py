# WAPP to unzip a list of tuples into individual lists

a = [(1,2),('a','b'),('@','#')]

b1 = []
b2 = []

for i,j in a:
    b1.append(i)
    b2.append(j)

print(f"Elements of first box : {b1}")
print(f"Elements of second box : {b2}")