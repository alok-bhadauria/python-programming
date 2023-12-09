#WAPP to find the length of a tuple

a = tuple(map(str, input("Enter tuple elements : ").split()))
cnt = 0
for _ in a:
    cnt += 1
print("Length of given tuple : ",cnt)