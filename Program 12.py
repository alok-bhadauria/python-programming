print("<== INPUT A LIST OF NUMBERS AND SWAP ELEMENTS LOCATION (even-odd)==>")

Lst = list(eval(input("Enter list elements : ")))
print("Original list : ", Lst)

a = len(Lst)

if a%2 != 0:
    a = a-1
for i in range(0,a,2):
    Lst[i],Lst[i+1]=Lst[i+1],Lst[i]

print("Swapped list : ",Lst)
