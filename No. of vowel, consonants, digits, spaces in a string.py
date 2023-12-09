string = input("Enter string : ")
Vowel = 'aeiouAEIOU'
V, C, D, Ws, Sp = 0,0,0,0,0
for i in string:
    if i in Vowel:
        V+=1
    elif ( ('a'<=i<='z' or 'A'<=i<='Z') and ( i not in Vowel) ):
        C+=1
    elif i == ' ':
        Ws+=1
    elif '0' <= i <= '9':
        D+=1
    else:
        Sp+=1
print('Vowels :',V,'\nConsonants :',C,'\nDigits :',D,'\nWhite Spaces :',Ws,'\nSpecial Characters :',Sp)
