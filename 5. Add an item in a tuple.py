# WAPP to add an item in a tuple

a = ('a','b','c','d')
print("Tuple : ",a)
b = input("Enter item to be added : ")
a=list(a)
a.append(b)
a=tuple(a)
print("New tuple : ",a)