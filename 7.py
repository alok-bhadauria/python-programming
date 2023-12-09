def series3(n):
    sum=0
    for i in range(1,n+1):
        sum += i**2
    return sum 

print(series3(int(input('Enter No. of terms upto which series is summed up :'))))
