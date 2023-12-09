def Insertionsort(n):
    alist=[]
    for i in range(0, n):
        if i==0:
            ele = int(input('Enter ' +str(i+1) +'st element: '))
        elif i==1:
            ele = int(input('Enter ' +str(i+1) +'nd element: '))
        elif i==2:
            ele = int(input('Enter ' +str(i+1) +'rd element: '))
        else :
            ele = int(input('Enter ' +str(i+1) +'th element: '))
        alist.append(ele) # adding the element
    print('List before sorting :',alist)
    for i in range(1,len(alist)):
        key = alist[i]
        j = i-1        
        while j>=0 and key < alist[j]:
            alist[j+1] = alist[j]
            j = j-1        
        else:
            alist[j+1]= key        
    print('List after sorting:',alist)
Insertionsort(int(input('Enter no of elements to be sort ')))
