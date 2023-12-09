a = {"A":1, "B":2, "C":3}
b = {"C":4, "D":5, "E":6}

# Method 1
a.update(b)
print(a)

# Method 2
for key,val in b.items():
    print(key,val)