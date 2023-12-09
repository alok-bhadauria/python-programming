# WAPP to convert a tuple to string

# Method 1 (for loop)
a = ('a','b','c','d','e')
b = ''
for i in a:
    b+=i
print(b,type(b))

# Method 2 (join)
a = ('a','b','c',1,2,3)
b = ''
b = b.join(map(str,a))
print(b,type(b))