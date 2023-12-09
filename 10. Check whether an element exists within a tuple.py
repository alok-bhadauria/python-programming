# 2. WAPP to check whether an element exists within a tuple

a = ('a','b','c','d','e',1,2,3,4,5)
b = input("Enter item to find within tuple : ")
if b in a:
    print("Element found at index : ",a.index(b))
elif eval(b) in a:
    print("Element found at index : ",a.index(eval(b)))
else:
    print("Element not found !")