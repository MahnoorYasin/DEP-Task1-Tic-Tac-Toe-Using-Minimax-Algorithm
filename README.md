# Tic Tac Toe with AI 

## Overview

A classic Tic Tac Toe game implemented with a graphical user interface (GUI) using Python's Tkinter library. The game includes an AI opponent powered by the Minimax algorithm for optimal gameplay.

## Features

- **Graphical User Interface (GUI):** Built using Tkinter.
- **AI Opponent:** Uses the Minimax algorithm for challenging gameplay.
- **Game Restart:** Easy option to restart the game.
- **Win and Draw Detection:** Displays results on the screen.

## How to Play

1. **Start the game:** Launch the game by running the Python script.
2. **Make a move:** Click on any square to place your mark (X).
3. **AI's turn:** The AI will make its move after yours.
4. **Win, Lose, or Draw:** The game displays the result.
5. **Restart the game:** Click "Restart Game" to play again.

## Code Overview

### GUI Setup

- **Main Window:** The main window (`root`) is set with a title and dimensions.
- **Board Layout:** Buttons are arranged in a 3x3 grid to represent the Tic Tac Toe board.

### Game Logic

- **Board State:** The board is represented by a dictionary with keys 1-9.
- **Turn and Game State:** Variables `turn` and `game_end` track the current turn and game status.
- **Minimax Algorithm:** AI uses the Minimax algorithm to make optimal moves.
- **Move Handling:** The `play` function updates the board and checks for win/draw conditions.
- **Restart Game:** The `restart_game` function resets the board and UI for a new game.


