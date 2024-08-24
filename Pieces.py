import random
colors = ["white","black"]
types = ["pawn","rook","knight","bishop","queen","king"]
class Piece:

    def __init__(self,color,type,position):
        self.color = color
        self.type = type
        self.position = position
    
    def move(self,pos):
        self.position = pos
 
    def __str__(self):
        letters = ["A","B","C","D","E","F","G","H"]
        return self.color + " " + self.type + " " + str(letters[self.position[0]]) + str(self.position[1]+1)

    def is_valid(self):
        pass
  
if __name__ == "__main__":
    piece = Piece(colors[random.randrange(2)-1],types[random.randrange(6)-1],(random.randrange(8),random.randrange(8)))
    print(piece)

# dunder methods in python (double underscore methods) run instantly in a class, __str__ method is an underlying method in every class (i.e; int())
