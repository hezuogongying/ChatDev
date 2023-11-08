'''
This is the main file of the Gomoku Game application. It initializes the game and starts the GUI.
'''
import tkinter as tk
from game import Game
from board import Board
from player import Player
class GomokuApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gomoku Game")
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.game = Game(self.board, self.player1, self.player2)
        self.create_gui()
    def create_gui(self):
        # Create the GUI elements here
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
    def on_click(self, event):
        # Get the clicked position
        x = event.x
        y = event.y
        # Calculate the row and column based on the clicked position
        row = y // 33
        col = x // 33
        # Make a move on the game board
        self.game.make_move(row, col)
        # Draw the game board
        self.draw_board()
        # Check for a winner
        winner = self.game.check_winner()
        if winner:
            self.show_winner(winner)
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(15):
            for col in range(15):
                piece = self.board.get_piece(row, col)
                if piece:
                    x = col * 33 + 16
                    y = row * 33 + 16
                    self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="black" if piece == "X" else "white")
    def show_winner(self, winner):
        self.canvas.delete("all")
        self.canvas.create_text(250, 250, text=f"{winner.get_name()} wins!", font=("Arial", 24), fill="red")
    def start(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = GomokuApp()
    app.start()