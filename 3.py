A=input('Enter first String ')
B=input('Enter Second String ')

A=A.split()
B=B.split()
x=[]
for i in A:
    if i not in B:
       x.append(i)
for i in B:
   if i not in A:
      x.append(i)
x=list(set(x))
print(x)
