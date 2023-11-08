'''
This file contains the Player class which represents a player in the game.
'''
class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    def get_name(self):
        return self.name
    def get_piece(self):
        return self.piece