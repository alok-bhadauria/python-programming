str1 = input("Enter text ")
n = int(input("Enter index "))
first_part = str1[:n] 
last_part = str1[n+1:]
print(first_part + last_part)
