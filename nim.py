def display_board(rows):
  for i, sticks in enumerate(rows, 1):
      print(" " * (len(rows) - i) + " ".join("|" * sticks))

def is_game_over(rows):
  return all(sticks == 0 for sticks in rows)

def available_moves(rows):
  moves = []
  for i, sticks in enumerate(rows, 1):
      for j in range(1, sticks + 1):
          moves.append((i, j))
  return moves

def make_move(rows, move):
  row, num_sticks = move
  rows[row - 1] -= num_sticks

def evaluate(rows):
  xor_sum = 0
  for sticks in rows:
      xor_sum ^= sticks
  return xor_sum

def minimax(rows, depth, maximizing_player):
  if depth == 0 or is_game_over(rows):
      return evaluate(rows)

  if maximizing_player:
      max_eval = float('-inf')
      for move in available_moves(rows):
          new_rows = rows.copy()
          make_move(new_rows, move)
          eval = minimax(new_rows, depth - 1, False)
          max_eval = max(max_eval, eval)
      return max_eval
  else:
      min_eval = float('inf')
      for move in available_moves(rows):
          new_rows = rows.copy()
          make_move(new_rows, move)
          eval = minimax(new_rows, depth - 1, True)
          min_eval = min(min_eval, eval)
      return min_eval

def get_user_move(rows, player_name):
  while True:
      try:
          print(f"{player_name}'s turn:")
          row = int(input("Enter the row number: "))
          sticks = int(input("Enter the number of sticks to take: "))
          if 1 <= row <= len(rows) and 1 <= sticks <= rows[row - 1]:
              return row, sticks
          else:
              print("Invalid move. Try again.")
      except ValueError:
          print("Invalid input. Please enter integers.")

def main():
  print("WELCOME TO NIM (PLAYER VS COMPUTER)")
  num_rows = int(input("Enter the number of rows of sticks: "))
  player_name = input("Player name: ")
  rows = [i for i in range(1, num_rows + 1)]  # Initial number of sticks in each row
  display_board(rows)

  while not is_game_over(rows):
      user_move = get_user_move(rows, player_name)
      make_move(rows, user_move)
      display_board(rows)

      if is_game_over(rows):
          print(f"Congratulations, {player_name}! You win!")
          break

      print("Computer's turn...")
      best_move = None
      best_eval = float('-inf')
      for move in available_moves(rows):
          new_rows = rows.copy()
          make_move(new_rows, move)
          eval = minimax(new_rows, 3, False)
          if eval > best_eval:
              best_eval = eval
              best_move = move

      print(f"Computer takes {best_move[1]} sticks from row {best_move[0]}.")
      make_move(rows, best_move)
      display_board(rows)

      if is_game_over(rows):
          print("Computer wins. Better luck next time!")

if _name_ == "_main_":
  main()
