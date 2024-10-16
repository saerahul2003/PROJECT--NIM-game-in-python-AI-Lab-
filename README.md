# PROJECT--NIM-game-in-python-AI-Lab-


display_board(rows):

Displays the current game board.
Each row is represented by sticks (|) with appropriate spacing to visually represent the game state.
is_game_over(rows):

Checks if the game is over by verifying if all rows are empty (all sticks removed).
Returns True if all rows have zero sticks, otherwise False.
available_moves(rows):

Generates all possible valid moves.
For each row, it adds moves for each possible number of sticks that can be taken from the row. The result is a list of possible moves in the form (row, number_of_sticks).
make_move(rows, move):

Modifies the game state by removing a specified number of sticks from a particular row based on the given move.
evaluate(rows):

Computes the XOR sum of the stick counts in all rows, which is a key concept in the optimal strategy of the Nim game (Nim-sum). A non-zero XOR value typically indicates that the current player has a winning strategy.
minimax(rows, depth, maximizing_player):

Implements the Minimax algorithm, which is used by the computer to decide its moves.
The algorithm recursively evaluates moves to choose the optimal one for the computer.
maximizing_player is True for the human player and False for the computer.
If the depth is 0 or the game is over, the current game state is evaluated with the evaluate() function.
The algorithm simulates each move, choosing the best one for both players.
get_user_move(rows, player_name):

Prompts the player for their move by asking for a row and the number of sticks to remove.
It ensures the player makes a valid move by checking the input against the current game state.
main():

Handles the game loop, including player and computer turns:
It starts by initializing the game with a specified number of rows, and each row starts with an increasing number of sticks (row 1 has 1 stick, row 2 has 2 sticks, etc.).
The player and computer take turns removing sticks.
After each move, the game state is checked. If the player removes the last stick, they win. If the computer does, the player loses.
Player's Turn:

The player makes a move via get_user_move(), and the board is updated using make_move() and displayed.
Computer's Turn:

The computer evaluates the best possible move using the minimax() function (with a depth limit of 3).
It selects the move that maximizes its chances of winning, removes the sticks, and updates the board.
if _name_ == "_main_":

Ensures that the main() function runs if the script is executed directly.
How the Game Works:
The player starts by choosing the number of rows of sticks.
The player and the computer alternate turns, with the player selecting the row and number of sticks to take.
The computer uses the Minimax algorithm to make optimal moves.
The game ends when all sticks are removed from the board, and the winner is declared based on who forces the other to take the last stick.
