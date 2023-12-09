# WAPP to remove an item from a tuple

a = tuple(map(str, input("Enter tuple items : ").split()))
print("Tuple formed : ",a)
b = input("Enter item to be removed : ")
a = list(a)
a.remove(b)
a = tuple(a)
print("New tuple : ",a)