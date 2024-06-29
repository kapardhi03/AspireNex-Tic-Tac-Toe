# AspireNex-Tic-Tac-Toe
 

This project implements an unbeatable Tic-Tac-Toe AI using the Minimax algorithm, with a user-friendly Streamlit interface for human players to challenge the AI.

## Features

- Unbeatable AI opponent using the Minimax algorithm
- Interactive web interface built with Streamlit
- Visually appealing game board with clear user feedback
- Game state management (win, lose, draw)
- Option to start a new game at any time

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/tictactoe-ai.git
   cd tictactoe-ai
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Tic-Tac-Toe game:

1. Navigate to the project directory in your terminal.
2. Run the following command:
   ```
   streamlit run app.py
   ```
3. Your default web browser should open automatically with the game interface.
4. If it doesn't open automatically, you can access the game by going to `http://localhost:8501` in your web browser.

or 

Directly access the game by clicking this [Link](https://aspirenex-tic-tac-toe.onrender.com/)

## How to Play

1. The game board is a 3x3 grid.
2. You play as 'O', and the AI plays as 'X'.
3. Click on any empty cell to make your move.
4. The AI will automatically make its move after you.
5. The goal is to get three of your symbols in a row (horizontally, vertically, or diagonally).
6. The game ends when either player wins or it's a draw.
7. Click "New Game" to reset the board and start over.

## Project Structure

- `app.py`: The main Streamlit application file containing the game interface and logic.
- `tictactoe_ai.py`: Contains the AI logic including the Minimax algorithm implementation.
- `requirements.txt`: Lists the Python packages required to run the project.

## AI Algorithm

The AI uses the Minimax algorithm to determine the best move:

1. It explores all possible moves from the current game state.
2. For each move, it recursively considers all possible counter-moves.
3. It evaluates terminal states (win, lose, draw) with scores.
4. The AI chooses the move that leads to the best possible outcome, assuming optimal play from both sides.

This makes the AI unbeatable - it will always win if possible, force a draw if it can't win, and never lose.

