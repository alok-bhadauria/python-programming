def bubblesort(n):
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

    n=len(alist)
    for i in range(n):
        for j in range(0,n-i-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]

    print('List after sorting:',alist)
bubblesort(int(input('Enter no of elements to be sort ')))
