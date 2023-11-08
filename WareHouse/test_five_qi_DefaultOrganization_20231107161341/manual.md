# Five Character Chess Game Program

## Introduction

The Five Character Chess Game Program is a Python application that allows you to play a simplified version of chess on a 5x5 board. The game follows the standard rules of chess, but with only five pieces per player.

## Installation

To install the Five Character Chess Game Program, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone or download the code from the GitHub repository: [https://github.com/chatdev-team/five-character-chess](https://github.com/chatdev-team/five-character-chess)

3. Open a terminal or command prompt and navigate to the directory where you downloaded the code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To start the Five Character Chess Game Program, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the code.

2. Activate the virtual environment (if you created one) by running the appropriate command for your operating system:

   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Run the main.py file by running the following command:

   ```
   python main.py
   ```

4. The game window will open, and you can start playing by clicking on the buttons representing the chess pieces on the board.

5. To make a move, click on a piece and then click on the destination square. Valid moves will be highlighted in green.

6. The game will continue until one player wins or it's a draw. The winner or draw result will be displayed in a message box.

## Game Rules

The Five Character Chess Game follows the standard rules of chess, with the following modifications:

- The game is played on a 5x5 board.
- Each player has only five pieces: Pawn (P), Rook (R), Knight (N), Bishop (B), and Queen (Q).
- The King (K) is not included in this version of the game.
- Pawns can only move forward one square at a time.
- Pawns can promote to any other piece when they reach the opposite end of the board.
- The game ends when one player captures all of the opponent's pieces or it's a draw.

## Customization

If you want to customize the game, you can modify the code in the main.py and game.py files. Here are some possible modifications:

- Change the appearance of the game board by modifying the create_board method in the ChessGameGUI class.
- Modify the piece movement rules by modifying the get_valid_moves_for_piece methods in the Game class.
- Add new pieces or change the existing pieces by modifying the Piece class and its subclasses in the piece.py file.

## Conclusion

The Five Character Chess Game Program is a fun and challenging game that allows you to play a simplified version of chess. Enjoy playing and exploring the possibilities of this unique chess variant!