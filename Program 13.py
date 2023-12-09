print("<== INPUT A LIST AND SEARCH FOR A GIVEN ELEMENT IN IT ==>")

Lst = list(eval(input("Enter numbers for list : ")))

a = int(input("Enter element to be searched : "))

x = len(Lst)

for i in range(x):
    if a == Lst[i]:
        print("Element found at index : ",i)
