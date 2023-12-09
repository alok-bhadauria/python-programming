def isEmpty( stk ):
    if stk == []:
        return True
    else :
        return False
def Push(stk,item) :
    stk.append(item)
    top = len(stk)-1
def Pop(stk) :
    if isEmpty(stk):
        return 'Underflow'
    else :
        item = stk.pop()
        if len( stk ) == 0:
            top =None
        else :
            top = len( stk )-1
        return item
Stack=[]
str2=''
str1 = input('Enter string ')

for i in str1:
    Push(Stack,i)
for j in range(len(Stack)):
    str2+=Pop(Stack)

print('Reversed string is :'+str2)
