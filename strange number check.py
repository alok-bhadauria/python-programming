n = int(input("Enter the number : "))
for i in range(2,n):
    if n % i == 0:
        flag = 1
        for j in range(2,i):
            if i % j == 0:
                flag = 0
                break
        if flag == 0:
            print("Not strange !")
            break
        st = i
else:
    if st > n**0.5:
         print("Strange !")
    else:
        print("Not strange !")