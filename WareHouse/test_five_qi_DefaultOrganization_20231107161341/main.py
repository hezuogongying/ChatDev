'''
This is the main file of the five character chess game program.
'''
import tkinter as tk
from game import Game
class ChessGameGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Five Character Chess Game")
        self.geometry("800x600")
        self.game = Game()
        self.create_board()
    def create_board(self):
        # Create the chess board GUI here
        self.board_frame = tk.Frame(self)
        self.board_frame.pack()
        self.buttons = []
        for i in range(5):
            row_buttons = []
            for j in range(5):
                button = tk.Button(self.board_frame, text=self.game.get_board_state()[i][j], width=10, height=5)
                button.grid(row=i, column=j)
                button.bind("<Button-1>", self.handle_click)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        self.start_game()
    def handle_click(self, event):
        # Handle the click event on the chess board GUI here
        button = event.widget
        row = button.grid_info()["row"]
        col = button.grid_info()["column"]
        move = self.game.get_valid_moves()[row * 5 + col]
        self.make_move(move)
    def start_game(self):
        # Start the game here
        self.game.start_game()
    def make_move(self, move):
        # Make a move in the game here
        piece, start, end = move
        self.game.make_move(move)
        self.buttons[start[0]][start[1]].configure(text=' ')
        self.buttons[end[0]][end[1]].configure(text=piece)
        if self.is_game_over():
            self.show_winner()
    def is_game_over(self):
        # Check if the game is over here
        return self.game.is_game_over()
    def get_winner(self):
        # Get the winner of the game here
        return self.game.get_winner()
    def get_board_state(self):
        # Get the current board state here
        return self.game.get_board_state()
    def get_valid_moves(self):
        # Get the valid moves for the current player here
        return self.game.get_valid_moves()
    def show_winner(self):
        winner = self.get_winner()
        if winner is not None:
            tk.messagebox.showinfo("Game Over", f"The winner is {winner}!")
        else:
            tk.messagebox.showinfo("Game Over", "It's a draw!")
if __name__ == "__main__":
    chess_game_gui = ChessGameGUI()
    chess_game_gui.mainloop()