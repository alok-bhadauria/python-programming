n = int(input("Enter no. of rows : "))

# Left forward triangle
for i in range(n):
    print(i*'*',end="\n")

#Left backward triangle
for i in range(n):
    print((n-i)*'*',end="\n")

#Right forward triangle
for i in range(n):
    print((n-i)*' ',i*'*',end="\n")

#Right backward triangle
for i in range(n):
    print(i*' ',(n-i)*'*',end="\n")

