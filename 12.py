upperCount =0
F=open("abcdef.txt","r")
while(True):
    data=F.read(1)
    if(data==""):
        break
    if (ord(data) >= 65 and ord(data) <= 90): 
        upperCount = upperCount +1
print(data,end='')
        
print("Total Upper Case:",upperCount)

F.close()
