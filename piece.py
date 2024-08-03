#board.py

class piece:
    def __init__(self, color, type, pos):
        self.color = color
        self.type = type
        self.position = [2, 3]

    def move(self, pos):
        self.position = pos

    def __str__(self):
        return self.color + " " + self.type + " at " + str(self.position[0]) + str(self.position[1])
    
if __name__ == "__main__":
    a = int(4)
    p = piece()
    print(p)