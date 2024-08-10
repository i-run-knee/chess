# This function returns True if the king is in check and
# returns False if the king is not in check
def kingincheck(board,color,pos):
    x = pos[0]
    y = pos[1]
    left_found = False
    right_found = False
    for c in range(1,8):
        left_pos=x+c
        if x+c<8 and not left_found:
            #check if pos is empty
            left_piece = board[left_pos][y]
            left_found = True
        right_pos=x-c
        if x-c>=0 and not right_found:
            #check if pos is empty
            right_piece = board[right_pos][y]
            right_found = True
        if left_piece.color != color:
            if left_piece.type == 'r':
                return True
        if right_piece.color != color:
            if right_piece.type == 'r':
                return True
        else:
            return False
