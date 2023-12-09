a,b=input().split()
a=int(a)
b=int(b)
k=int(input())

x=a&b
y=a|b
z=a^b

x = x * (x<k)
y = y * (y<k)
z = z * (z<k)

print(max(x,y,z))
