from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board = self._create_board()
        self._setup_pieces()

    def _create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        return board

    def _setup_pieces(self):
        # White pieces
        for i in range(8):
            self.board[6][i] = Pawn("white", (6, i))
        self.board[7][0] = Rook("white", (7, 0))
        self.board[7][7] = Rook("white", (7, 7))
        self.board[7][1] = Knight("white", (7, 1))
        self.board[7][6] = Knight("white", (7, 6))
        self.board[7][2] = Bishop("white", (7, 2))
        self.board[7][5] = Bishop("white", (7, 5))
        self.board[7][3] = Queen("white", (7, 3))
        self.board[7][4] = King("white", (7, 4))

        # Black pieces
        for i in range(8):
            self.board[1][i] = Pawn("black", (1, i))
        self.board[0][0] = Rook("black", (0, 0))
        self.board[0][7] = Rook("black", (0, 7))
        self.board[0][1] = Knight("black", (0, 1))
        self.board[0][6] = Knight("black", (0, 6))
        self.board[0][2] = Bishop("black", (0, 2))
        self.board[0][5] = Bishop("black", (0, 5))
        self.board[0][3] = Queen("black", (0, 3))
        self.board[0][4] = King("black", (0, 4))

    def display(self):
        for row in self.board:
            print(" ".join([str(piece) if piece is not None else "." for piece in row]))

    def move_piece(self, start_pos, end_pos):
        piece = self.board[start_pos[0]][start_pos[1]]
        if piece is None:
            return False

        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = None
        piece.set_position(end_pos)
        return True
