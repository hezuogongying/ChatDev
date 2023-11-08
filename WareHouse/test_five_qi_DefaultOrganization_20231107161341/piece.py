'''
This file contains the Piece class and its subclasses which represent the different chess pieces.
'''
class Piece:
    def __init__(self, color):
        # Initialize the piece with the given color here
        self.color = color
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the piece at the given position on the board state here
        pass
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the pawn at the given position on the board state here
        valid_moves = []
        row, col = position
        if self.color == 'W':
            if row > 0 and board_state[row - 1][col] == ' ':
                valid_moves.append(('P', position, (row - 1, col)))
            if row == 4 and board_state[row - 1][col] == ' ' and board_state[row - 2][col] == ' ':
                valid_moves.append(('P', position, (row - 2, col)))
        else:
            if row < 4 and board_state[row + 1][col] == ' ':
                valid_moves.append(('P', position, (row + 1, col)))
            if row == 0 and board_state[row + 1][col] == ' ' and board_state[row + 2][col] == ' ':
                valid_moves.append(('P', position, (row + 2, col)))
        return valid_moves
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the rook at the given position on the board state here
        valid_moves = []
        row, col = position
        # Check valid moves in the same row
        for i in range(col + 1, 5):
            if board_state[row][i] == ' ':
                valid_moves.append(('R', position, (row, i)))
            else:
                break
        for i in range(col - 1, -1, -1):
            if board_state[row][i] == ' ':
                valid_moves.append(('R', position, (row, i)))
            else:
                break
        # Check valid moves in the same column
        for i in range(row + 1, 5):
            if board_state[i][col] == ' ':
                valid_moves.append(('R', position, (i, col)))
            else:
                break
        for i in range(row - 1, -1, -1):
            if board_state[i][col] == ' ':
                valid_moves.append(('R', position, (i, col)))
            else:
                break
        return valid_moves
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the knight at the given position on the board state here
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
            if 0 <= move[0] < 5 and 0 <= move[1] < 5 and board_state[move[0]][move[1]] == ' ':
                valid_moves.append(('N', position, move))
        return valid_moves
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the bishop at the given position on the board state here
        valid_moves = []
        row, col = position
        # Check valid moves in the diagonal directions
        # Top-left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i -= 1
            j -= 1
        # Top-right
        i, j = row - 1, col + 1
        while i >= 0 and j < 5:
            if board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i -= 1
            j += 1
        # Bottom-left
        i, j = row + 1, col - 1
        while i < 5 and j >= 0:
            if board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i += 1
            j -= 1
        # Bottom-right
        i, j = row + 1, col + 1
        while i < 5 and j < 5:
            if board_state[i][j] == ' ':
                valid_moves.append(('B', position, (i, j)))
            else:
                break
            i += 1
            j += 1
        return valid_moves
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the queen at the given position on the board state here
        valid_moves = []
        row, col = position
        # Check valid moves in the same row
        for i in range(col + 1, 5):
            if board_state[row][i] == ' ':
                valid_moves.append(('Q', position, (row, i)))
            else:
                break
        for i in range(col - 1, -1, -1):
            if board_state[row][i] == ' ':
                valid_moves.append(('Q', position, (row, i)))
            else:
                break
        # Check valid moves in the same column
        for i in range(row + 1, 5):
            if board_state[i][col] == ' ':
                valid_moves.append(('Q', position, (i, col)))
            else:
                break
        for i in range(row - 1, -1, -1):
            if board_state[i][col] == ' ':
                valid_moves.append(('Q', position, (i, col)))
            else:
                break
        # Check valid moves in the diagonal directions
        # Top-left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i -= 1
            j -= 1
        # Top-right
        i, j = row - 1, col + 1
        while i >= 0 and j < 5:
            if board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i -= 1
            j += 1
        # Bottom-left
        i, j = row + 1, col - 1
        while i < 5 and j >= 0:
            if board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i += 1
            j -= 1
        # Bottom-right
        i, j = row + 1, col + 1
        while i < 5 and j < 5:
            if board_state[i][j] == ' ':
                valid_moves.append(('Q', position, (i, j)))
            else:
                break
            i += 1
            j += 1
        return valid_moves
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_valid_moves(self, position, board_state):
        # Get the valid moves for the king at the given position on the board state here
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
            if 0 <= move[0] < 5 and 0 <= move[1] < 5 and board_state[move[0]][move[1]] == ' ':
                valid_moves.append(('K', position, move))
        return valid_moves