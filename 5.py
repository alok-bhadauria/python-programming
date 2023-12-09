def series1(n):
    sum = sum1 = 0
    for i in range(1,n+1):
        sum = sum1 = 0
        for j in range(1,i+1):
            sum += j
            sum1 += sum
    return sum1
print(series1(int(input('Enter No. of terms upto which series is summed up :'))))
