'''
This file contains the Game class which represents the game logic of the five character chess game.
'''
import tkinter as tk
class Game:
    def __init__(self):
        # Initialize the game state here
        self.board_state = [[' ' for _ in range(5)] for _ in range(5)]
        self.current_player = 'W'
        self.game_over = False
        self.winner = None
    def start_game(self):
        # Start the game here
        self.board_state = [[' ' for _ in range(5)] for _ in range(5)]
        self.current_player = 'W'
        self.game_over = False
        self.winner = None
    def make_move(self, move):
        # Make a move in the game here
        piece, start, end = move
        self.board_state[end[0]][end[1]] = piece
        self.board_state[start[0]][start[1]] = ' '
        self.current_player = 'B' if self.current_player == 'W' else 'W'
    def is_game_over(self):
        # Check if the game is over here
        return self.game_over
    def get_winner(self):
        # Get the winner of the game here
        return self.winner
    def get_board_state(self):
        # Get the current board state here
        return self.board_state
    def get_valid_moves(self):
        # Get the valid moves for the current player here
        valid_moves = []
        for i in range(5):
            for j in range(5):
                if self.board_state[i][j] == self.current_player:
                    piece = self.board_state[i][j]
                    valid_moves.extend(self.get_valid_moves_for_piece(piece, (i, j)))
        return valid_moves
    def get_valid_moves_for_piece(self, piece, position):
        valid_moves = []
        if piece == 'P':
            valid_moves.extend(self.get_valid_moves_for_pawn(position))
        elif piece == 'R':
            valid_moves.extend(self.get_valid_moves_for_rook(position))
        elif piece == 'N':
            valid_moves.extend(self.get_valid_moves_for_knight(position))
        elif piece == 'B':
            valid_moves.extend(self.get_valid_moves_for_bishop(position))
        elif piece == 'Q':
            valid_moves.extend(self.get_valid_moves_for_queen(position))
        elif piece == 'K':
            valid_moves.extend(self.get_valid_moves_for_king(position))
        return valid_moves
    def get_valid_moves_for_pawn(self, position):
        valid_moves = []
        row, col = position
        if self.current_player == 'W':
            if row > 0 and self.board_state[row - 1][col] == ' ':
                valid_moves.append(('P', position, (row - 1, col)))
            if row == 4 and self.board_state[row - 1][col] == ' ' and self.board_state[row - 2][col] == ' ':
                valid_moves.append(('P', position, (row - 2, col)))
        else:
            if row < 4 and self.board_state[row + 1][col] == ' ':
                valid_moves.append(('P', position, (row + 1, col)))
            if row == 0 and self.board_state[row + 1][col] == ' ' and self.board_state[row + 2][col] == ' ':
                valid_moves.append(('P', position, (row + 2, col)))
        return valid_moves
    def get_valid_moves_for_rook(self, position):
        valid_moves = []
        row, col = position
        # Check valid moves in the same row
        for i in range(col + 1, 5):
            if self.board_state[row][i] == ' ':
                valid_moves.append(('R', position, (row, i)))
            else:
                break
        for i in range(col - 1, -1, -1):
            if self.board_state[row][i] == ' ':
                valid_moves.append(('R', position, (row, i)))
            else:
                break
        # Check valid moves in the same column
        for i in range(row + 1, 5):
            if self.board_state[i][col] == ' ':
                valid_moves.append(('R', position, (i, col)))
            else:
                break
        for i in range(row - 1, -1, -1):
            if self.board_state[i][col] == ' ':
                valid_moves.append(('R', position, (i, col)))
            else:
                break
        return valid_moves
    def get_valid_moves_for_knight(self, position):
        valid_moves = []
        row, col = position
        moves = [
            (row - 2, col - 1),
            (row - 2, col + 1),
            (row - 1, col - 2),
            (row - 1, col + 2),
            (row + 1, col - 2),
            (row + 1, col + 2),
            (row + 2, col - 1),
            (row + 2, col + 1)
        ]
        for move in moves:
            if 0 <= move[0] < 5 and 0 <= move[1] < 5 and self.board_state[move[0]][move[1]] == ' ':
                valid_moves.append(('N', position, move))
        return valid_moves
    def get_valid_moves_for_bishop(self, position):
        valid_moves = []
        row, col = position
        # Check valid moves in the diagonal directions
        # Top-left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i -= 1
            j -= 1
        # Top-right
        i, j = row - 1, col + 1
        while i >= 0 and j < 5:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i -= 1
            j += 1
        # Bottom-left
        i, j = row + 1, col - 1
        while i < 5 and j >= 0:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i += 1
            j -= 1
        # Bottom-right
        i, j = row + 1, col + 1
        while i < 5 and j < 5:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i += 1
            j += 1
        return valid_moves
    def get_valid_moves_for_queen(self, position):
        valid_moves = []
        row, col = position
        # Check valid moves in the same row
        for i in range(col + 1, 5):
            if self.board_state[row][i] == ' ':
                valid_moves.append(('Q', position, (row, i)))
            else:
                break
        for i in range(col - 1, -1, -1):
            if self.board_state[row][i] == ' ':
                valid_moves.append(('Q', position, (row, i)))
            else:
                break
        # Check valid moves in the same column
        for i in range(row + 1, 5):
            if self.board_state[i][col] == ' ':
                valid_moves.append(('Q', position, (i, col)))
            else:
                break
        for i in range(row - 1, -1, -1):
            if self.board_state[i][col] == ' ':
                valid_moves.append(('Q', position, (i, col)))
            else:
                break
        # Check valid moves in the diagonal directions
        # Top-left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i -= 1
            j -= 1
        # Top-right
        i, j = row - 1, col + 1
        while i >= 0 and j < 5:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i -= 1
            j += 1
        # Bottom-left
        i, j = row + 1, col - 1
        while i < 5 and j >= 0:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i += 1
            j -= 1
        # Bottom-right
        i, j = row + 1, col + 1
        while i < 5 and j < 5:
            if self.board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i += 1
            j += 1
        return valid_moves
    def get_valid_moves_for_king(self, position):
        valid_moves = []
        row, col = position
        moves = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1)
        ]
        for move in moves:
            if 0 <= move[0] < 5 and 0 <= move[1] < 5 and self.board_state[move[0]][move[1]] == ' ':
                valid_moves.append(('K', position, move))
        return valid_moves