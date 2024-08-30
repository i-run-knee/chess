def solve_n_queen(n, row, preboard):
    if row == 1:
        board = [0 for _ in range(n**2)]
    else:
        board = preboard[:] # create a new object in memory
    
    queens = []
    for x in range(n**2):
        if board[x] == 1:
            queens.append((x % n + 1, x // n + 1))

    if row > n:
        print(board)
        return True
    
    for y in range(n):
        printrow = []
        for x in range(n):
            get = board[x + y * n]  # Fixed index calculation here
            printrow.append(get)
        print(printrow)    
    print("")

    for x in range(n):
        if safe(queens, (x + 1, row)):
            savestate = board[:]  # Create a copy of the board
            savestate[x + n * (row - 1)] = 1
            if solve_n_queen(n, row + 1, savestate):  # Check if the solution was successful
                return True
            # If not successful, the function will backtrack
    
    return False  # Return False if no solution was found

def safe(queens, position):
    for coordinate in queens:
        if coordinate[0] == position[0] or abs(position[1] - coordinate[1]) == abs(position[0] - coordinate[0]):
            return False
    return True

solve_n_queen(int(input("rows:")), 1, [])
