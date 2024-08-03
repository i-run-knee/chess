class Piece:

    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position

    def move(self, position):
        self.position = position

    def __str__():
        pass

if __name__ == "__main__":
    piece = Piece("white", "rook", (0,0))
