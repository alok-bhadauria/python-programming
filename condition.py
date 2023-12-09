#write a python program to find the largest number among 3 variables

a, b, c = list(map(int, input("Enter numbers : ").split()))
print("Largest number : ",max(a,b,c))
