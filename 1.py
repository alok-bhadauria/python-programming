line = input("Enter line ")
substr = input("Enter substring ")
lenline = len(line)
lensub = len(substr)
start=count=0
end = lenline
while True:
    pos = line.find(substr,start,end)
    if pos !=-1:
        count +=1
        start = pos + lensub
    else :
        break
    if start >= lenline :
        break
print("No. of substring "+substr, ":",str(count))
