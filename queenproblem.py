def solve_n_queen(n,row,preboard):
    if row == 1:
        board = [0 for x in range(n**2)]
    else:
        board = preboard
    
    queens = []
    for x in range(n**2):
        if board[x] == 1:
            queens.append((x%n+1,int(x/n)+1))

    if row>n:
        print(board)
        return True
    
    for y in range(n):
        printrow = []
        for x in range(n):
            get = board[x+y*(row-1)]
            printrow.append(get)
        print(printrow)    
    print("")


    savestate = board
    for x in range(n):
        if safe(queens,(x+1,row)):
            board = savestate
            board[x+n*(row-1)] = 1
            solve_n_queen(n,row+1,board)

def safe(queens, position):
    for coordinate in queens:
        if coordinate[0] == position[0] or abs(position[1]-coordinate[1]) == abs(position[0]-coordinate[0]):
            return False
    return True
        

solve_n_queen(int(input("rows:")),1,[0,0,0,0])