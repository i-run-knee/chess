import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

# Load images
pieces = {}
for piece in ['bB', 'bK', 'bN', 'bP', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wP', 'wQ', 'wR']:
    pieces[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))

# Draw board
def draw_board():
    colors = [WHITE, BLACK]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# Create board matrix
def create_board():
    board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    ]
    return board

# Draw pieces
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                screen.blit(pieces[piece], (col*SQUARE_SIZE, row*SQUARE_SIZE))

def is_valid_move(board, piece, start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    if piece == 'wP':
        # White pawn movement
        if start_row == 6 and start_row - end_row == 2 and start_col == end_col and board[end_row][end_col] is None:
            return True
        if start_row - end_row == 1 and start_col == end_col and board[end_row][end_col] is None:
            return True
        if start_row - end_row == 1 and abs(start_col - end_col) == 1 and board[end_row][end_col] is not None and board[end_row][end_col][0] == 'b':
            return True
    elif piece == 'bP':
        # Black pawn movement
        if start_row == 1 and end_row - start_row == 2 and start_col == end_col and board[end_row][end_col] is None:
            return True
        if end_row - start_row == 1 and start_col == end_col and board[end_row][end_col] is None:
            return True
        if end_row - start_row == 1 and abs(start_col - end_col) == 1 and board[end_row][end_col] is not None and board[end_row][end_col][0] == 'w':
            return True
    # Add rules for other pieces
    return False

def main():
    board = create_board()
    running = True
    selected_piece = None
    selected_square = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE
                
                # When a piece is selected
                if selected_piece is None:
                    if board[row][col] is not None:
                        selected_piece = board[row][col]
                        selected_square = (row, col)
                else:
                    # Target square
                    target_square = (row, col)
                    if is_valid_move(board, selected_piece, selected_square, target_square):
                        # Make the move
                        board[selected_square[0]][selected_square[1]] = None
                        board[target_square[0]][target_square[1]] = selected_piece
                    # Reset selection
                    selected_piece = None
                    selected_square = None

        draw_board()
        draw_pieces(board)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
