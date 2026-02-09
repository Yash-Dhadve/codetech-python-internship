# Q2_TicTacToe_Simple.py
# Simple Tic-Tac-Toe game (Player X vs Player O)

# Function to print board
def print_board(board):
    print()
    for i in range(3):
        print(board[3*i], board[3*i+1], board[3*i+2])
    print()

# Check winner
def check_winner(board):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),        # rows
        (0,3,6), (1,4,7), (2,5,8),        # columns
        (0,4,8), (2,4,6)                  # diagonals
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] != "_":
            return board[a]
    return None

# Check if board is full
def is_full(board):
    return "_" not in board


# ------------ MAIN GAME ------------
board = ["_"] * 9
current = "X"

print("TIC-TAC-TOE GAME (Player X vs Player O)")
print_board(board)

while True:
    print("Player", current)
    move = int(input("Enter position (0-8): "))

    # Validate move
    if move < 0 or move > 8 or board[move] != "_":
        print("Invalid move! Try again.")
        continue

    board[move] = current
    print_board(board)

    # Check win
    winner = check_winner(board)
    if winner:
        print("Player", winner, "WINS!")
        break

    # Check draw
    if is_full(board):
        print("It's a DRAW!")
        break

    # Switch player
    current = "O" if current == "X" else "X"

