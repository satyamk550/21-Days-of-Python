def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "
        
        print(row_str)

        if i != len(board) - 1:
            print("-----")

def get_mov(turn, board):
    while True:
        row = int(input("row: ")) - 1 
        col = int(input("col: ")) - 1

        if row < 0 or row >= len(board):
            print("Invalid row. Please try again. ")
            continue
        elif col < 0 or col >= len(board[row]):
            print("Invalid col. Please try again. ")
            continue
            
        elif board[row][col] != " ":
            print("already taken. Please try again. ")
        else:
            board[row][col] = turn
            break

def check_winner(board, turn):
    lines = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break
        if win:
            return True
    return False

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
    print("Turn number: " + str(turn_number))
    print("it is your turn, " + turn + ". please select your move.")
    if turn =="0":
        get_mov(turn, board)
    print_board(board)
    winner = check_winner(board, turn)
    if winner:
        print(turn + " has won!")
        break
    
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1