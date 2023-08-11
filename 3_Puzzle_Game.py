import random

game_on = True
move = 0

alpha = [0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

random.shuffle(alpha)

matrix = []
while alpha != []:
    matrix.append(alpha[:5])
    alpha = alpha[5:]

def zero(board):
   global empty_space
   for x in range(len(board)):
       for y in range(len(board[x])):
           if board[x][y] == 0:
               empty_space = (x, y)

   return empty_space

def draw_board(board):
    print('\n\t+-------+-------+-------+-------+-------|')

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                print('\t|  ' , end =  '')
            else:
                 print('\t|  ' + '{}' .format(board[x][y]), end = ' ')
        print('\n\t+-------+-------+-------+-------+-------|')

def ask_alphabet():
    global alphabet , piece
    alphabet = input( '\nplease type the alphabet of the piece to move : ( q ) to quit  ')
    if alphabet == 'q':
        print('\n\ngame over') 
    piece = ()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if alphabet == matrix[i][j]:
                piece = (i, j)
    return piece, alphabet

zero(matrix)

while game_on:
    draw_board(matrix)      
    ask_alphabet()        
    if not alphabet in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','q'):
        print('Illegal move , try again')
    else:
        if(empty_space==(piece[0]-1,piece[1]))\
           or(empty_space==(piece[0]+1,piece[1]))\
           or(empty_space==(piece[0],piece[1]-1))\
           or(empty_space==(piece[0],piece[1]+1)):
            matrix[empty_space[0]][empty_space[1]]=alphabet
            matrix[piece[0]][piece[1]]=0
            empty_space=(piece[0],piece[1])
            move = move +1
            print('you have made ',move , 'moves so far\n ')
        else:
            print('Try again ')
