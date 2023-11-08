'''
This file contains the Game class which manages the game logic.
'''
class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.current_player = player1
        self.player1 = player1
        self.player2 = player2
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
    def make_move(self, row, col):
        if self.board.get_piece(row, col) is None:
            self.place_piece(row, col, self.current_player.get_piece())
            self.switch_player()
    def place_piece(self, row, col, piece):
        self.board.place_piece(row, col, piece)
    def check_winner(self):
        # Check rows
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[row]) - 4):
                if self.board.board[row][col] is not None:
                    if all(self.board.board[row][col] == self.board.board[row][col + i] for i in range(1, 5)):
                        return self.board.board[row][col]
        # Check columns
        for col in range(len(self.board.board[0])):
            for row in range(len(self.board.board) - 4):
                if self.board.board[row][col] is not None:
                    if all(self.board.board[row][col] == self.board.board[row + i][col] for i in range(1, 5)):
                        return self.board.board[row][col]
        # Check diagonals (top-left to bottom-right)
        for row in range(len(self.board.board) - 4):
            for col in range(len(self.board.board[row]) - 4):
                if self.board.board[row][col] is not None:
                    if all(self.board.board[row][col] == self.board.board[row + i][col + i] for i in range(1, 5)):
                        return self.board.board[row][col]
        # Check diagonals (top-right to bottom-left)
        for row in range(len(self.board.board) - 4):
            for col in range(4, len(self.board.board[row])):
                if self.board.board[row][col] is not None:
                    if all(self.board.board[row][col] == self.board.board[row + i][col - i] for i in range(1, 5)):
                        return self.board.board[row][col]
        return None
    def reset(self):
        self.board.reset()
        self.current_player = self.player1