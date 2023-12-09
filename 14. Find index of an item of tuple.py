# WAPP to find the index of an item of a tuple

a = tuple(map(str, input("Enter tuple elements : ").split()))
b = input(("Enter element to find index : "))
if b in a:
    print("Element at index : ", a.index(b))
else:
    print("Element not found !")