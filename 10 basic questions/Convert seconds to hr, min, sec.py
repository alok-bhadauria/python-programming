seconds = int(input("Enter number of seconds : "))
rem_sec = seconds%60
minutes = seconds//60
rem_min = minutes%60
hours = minutes//60

print("Given number of seconds : ",seconds)

print("<== After simplification ==>")

print("Hours : ",hours)
print("Minutes : ",rem_min)
print("Seconds : ",rem_sec)
