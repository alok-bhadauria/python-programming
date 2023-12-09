def checkChar():
    with open("abcdef.txt","r") as f1:
       data=f1.readlines()
    cnt_lines=0
    cnt_A=0
    cnt_B=0
    cnt_C=0
    for lines in data:
        cnt_lines+=1
        if lines[0]=='A':
            cnt_A+=1
        if lines[0]=='B':
            cnt_B+=1
        if lines[0]=='C':
            cnt_C+=1
    print("Total Number of lines are:",cnt_lines)
    print("Total Number of lines starting with A are:",cnt_A)
    print("Total Number of lines starting with B are:",cnt_B)
    print("Total Number of lines starting with C are:",cnt_C)
checkChar()
