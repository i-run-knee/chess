# n_queens.py

def solve_n_queen(n):
    pass

def is_safe(board,row,col):
    # Check for column
    for i in range(row):
        if board[i][col] == 1:
            return False
        else:
            return True
    # Check for left diagonal
    for i in range(row):
        if board[row-i][col-i] == 1:
            return False
        else:
            return True
    # Check for right diagonal
    for i in range(len(board[0])):
        if board[row-i][col+i] == 1:
            return False
        else:
            return True
def solve(board,row):
    pass
def print_solution_board(board):
    pass