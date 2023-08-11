import random
import tkinter as tk

game_on = True
move = 0

alpha = [0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
random.shuffle(alpha)
matrix = [alpha[i:i+5] for i in range(0, len(alpha), 5)]

empty_space = (0, 0)
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 0:
            empty_space = (x, y)
            break

def draw_board():
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            text = matrix[x][y] if matrix[x][y] != 0 else ' '
            buttons[x][y].config(text=text)

def move_piece(i, j):
    global move, empty_space
    if (i, j) == empty_space:
        return
    if (i == empty_space[0] and abs(j - empty_space[1]) == 1) or \
       (j == empty_space[1] and abs(i - empty_space[0]) == 1):
        matrix[empty_space[0]][empty_space[1]] = matrix[i][j]
        matrix[i][j] = 0
        empty_space = (i, j)
        move += 1
        move_label.config(text=f'Moves: {move}')
        draw_board()

def quit_game():
    global game_on
    game_on = False
    root.destroy()

root = tk.Tk()
root.title("Alphabet Puzzle Game")

buttons = [[None for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        buttons[i][j] = tk.Button(root, text='', width=5, height=2,
                                  command=lambda i=i, j=j: move_piece(i, j))
        buttons[i][j].grid(row=i, column=j, padx=2, pady=2)

move_label = tk.Label(root, text='Moves: 0')
move_label.grid(row=5, columnspan=5)

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.grid(row=6, columnspan=5)

draw_board()
root.mainloop()
