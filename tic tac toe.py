def display(x):
    print('''
 {0} | {1} | {2} 
___|___|___
 {3} | {4} | {5} 
___|___|___
 {6} | {7} | {8} 
   |   |   '''.format(*x))
    
move = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

display(move)

turn = 'X'
while 1:
    input1 = int(input(f'{turn} Turn index location (0-8): '))
    if move[input1] != ' ':
        print('Location already used \nTry another location ')
        continue
    else:
        move[input1] = turn
    display(move)
    if move[0] == move[1] == move[2] != ' ':
        print(f'{move[0]} Win !')
        break
    if move[3] == move[4] == move[5] != ' ':
        print(f'{move[3]} Win !')
        break
    if move[6] == move[7] == move[8] != ' ':
        print(f'{move[6]} Win !')
        break
    if move[0] == move[3] == move[6] != ' ':
        print(f'{move[0]} Win !')
        break
    if move[1] == move[4] == move[7] != ' ':
        print(f'{move[1]} Win !')
        break
    if move[2] == move[5] == move[8] != ' ':
        print(f'{move[2]} Win !')
        break
    if move[0] == move[4] == move[8] != ' ':
        print(f'{move[0]} Win !')
        break
    if move[2] == move[4] == move[6] != ' ':
        print(f'{move[2]} Win !')
        break
    if ' ' not in move:
        break
    turn = 'O' if turn =='X' else 'X'