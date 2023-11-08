'''
This file contains the Board class which represents the game board.
'''
class Board:
    def __init__(self):
        self.board = [[None] * 15 for _ in range(15)]
    def get_piece(self, row, col):
        return self.board[row][col]
    def place_piece(self, row, col, piece):
        self.board[row][col] = piece
    def is_full(self):
        for row in self.board:
            if None in row:
                return False
        return True
    def reset(self):
        self.board = [[None] * 15 for _ in range(15)]