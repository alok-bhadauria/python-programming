import time
n = int(input("Enter run time for timer : "))
print("START !")
while n:
    print(n)
    n-=1
    time.sleep(1)
print("TIME UP !")
