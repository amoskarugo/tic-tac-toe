import random

Game_on = True
new_game = True
message = ["You won!", "You lost!", "tie"]

#create an empty tic-tac-toe board with empty fields from 1-9
def creat_board():
    board = [[x for x in range(1, 4)] for j in range(3)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 1:
                board[i][j]  += 3
            if i == 2:
                board[i][j]  += 6
    return board
#print the board on the screen
def print_board(board):
    for row in range(5):
        if row % 2 == 0:
            for column in range(5):
                if column % 2 == 0:
                    print(board[int(row / 2)][int(column / 2)], end='')
                else:
                    print(' | ', end='')
        else:
            print()
    print()
#a fuction that checks and returns a list of all free fields
def _free(lst):
    new_list = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if str(lst[i][j]) not in "OX":
                tup = (i, j)
                new_list.append(tup)

    return new_list

#a function that allows the computer to make its move
def bot(_board):
        free_lst = _free(_board)
        ln = len(free_lst)
        if ln > 0:
            move = random.randrange(ln)
            x, y = free_lst[move]
            board[x][y] = "X"

def enter_move(board):
    try:
        move = int(input("Enter move: "))
    except:
        print("Enter a number")
        enter_move()
    if move < 1 or move > 9:
        print("Select a number based on the numbers on the Board")
        print_board(board)
        enter_move()
    for i in board:
        for j in range(len(i)):
            if i[j] == move:
                i[j] = "O"


def victory_for(board, sign):
    if sign == "X":
        winner = "bot"
    elif sign == "O":
        winner = "me"
    else:
        winner = None
    
    cross1 = cross2 = True
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:# CHECK ROW
            return winner
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: #CHECK COLUMN
            return winner
        if board[i][i] != sign:# check first diagonal
            cross1 = False
        if board[2 - i][2 - i] != sign: #check second diagnol
            cross2 = False
    if cross1 or cross2:
        return winner
    return None

board = creat_board()
board[1][1] = "X"
free = _free(board)
human_turn = True
while len(free):
    print_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, "O")
    else:
        bot(board)
        print("bot playing")
        victor = victory_for(board, "X")
    if victor != None:
        break
    human_turn = not human_turn	


print_board(board)
if victor == "bot":
    print(message[1])
elif victor == "me":
    print(message[0])
else:
    print(message[2])




