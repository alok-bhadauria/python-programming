print("<== APPLYING CONDITIONS IN DICTIONARY ==>")

A = int(input("Enter number of students : "))
B = {}
for i in range(A):
    print("Enter details of student no.",i+1)
    R = int(input("Roll no. : "))
    N = input("Name : ")
    M = int(input("Marks : "))
    B[R] = [N , M]
print("Dictionary created : ",B)

print("Students who scored above 75 : ")
for i in B:
    if B[i][1] > 75:
        print(B[i][0])
