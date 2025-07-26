from board import Board
from pieces import King

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.move_history = []

    def play(self):
        while not self.is_game_over():
            self.board.display()
            print(f"{self.turn}'s turn")
            move = input("Enter your move (e.g., e2e4): ")
            if move == "reset":
                self.reset()
                continue
            if self.is_valid_move(move):
                start_pos, end_pos = self._parse_move(move)
                self.board.move_piece(start_pos, end_pos)
                self.move_history.append(move)
                self.switch_turn()
            else:
                print("Invalid move")
        self.announce_winner()

    def is_game_over(self):
        kings = []
        for row in self.board.board:
            for piece in row:
                if isinstance(piece, King):
                    kings.append(piece)
        return len(kings) < 2

    def announce_winner(self):
        for row in self.board.board:
            for piece in row:
                if isinstance(piece, King):
                    print(f"{piece.get_color()} wins!")
                    return

    def reset(self):
        self.board = Board()
        self.turn = "white"
        self.move_history = []

    def is_valid_move(self, move):
        # Basic validation for now
        return len(move) == 4 and move[0].isalpha() and move[1].isdigit() and move[2].isalpha() and move[3].isdigit()

    def _parse_move(self, move):
        col_map = {chr(ord('a') + i): i for i in range(8)}
        start_col = col_map[move[0]]
        start_row = 8 - int(move[1])
        end_col = col_map[move[2]]
        end_row = 8 - int(move[3])
        return (start_row, start_col), (end_row, end_col)

    def switch_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

if __name__ == "__main__":
    game = Game()
    game.play()
