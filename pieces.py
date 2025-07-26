class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __str__(self):
        raise NotImplementedError

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

class Pawn(Piece):
    def __str__(self):
        return "\u2659" if self.color == "white" else "\u265F"

class Rook(Piece):
    def __str__(self):
        return "\u2656" if self.color == "white" else "\u265C"

class Knight(Piece):
    def __str__(self):
        return "\u2658" if self.color == "white" else "\u265E"

class Bishop(Piece):
    def __str__(self):
        return "\u2657" if self.color == "white" else "\u265D"

class Queen(Piece):
    def __str__(self):
        return "\u2655" if self.color == "white" else "\u265B"

class King(Piece):
    def __str__(self):
        return "\u2654" if self.color == "white" else "\u265A"
