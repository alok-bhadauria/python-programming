def series2(x,n):
    total = 1

    for i in range(1,n+1):
        num = i * 2
        fact = 1
        for j in range(1,num+1):
            fact = fact * j
        fraction = (x**i)/fact
        total = total + fraction
    return total

print(series2(int(input('Enter value of x variable :')),
              int(input('Enter No. of terms upto which series is summed up :'))))
