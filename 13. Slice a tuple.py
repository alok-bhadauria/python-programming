# WAPP to slice a tuple

a = tuple(map(str, input("Enter tuple elements : ").split()))
b = int(input("Enter index for slicing : "))
print("Sliced tuples at given index : ",end=" ")
print(a[0:b]," and ",a[b:-1])