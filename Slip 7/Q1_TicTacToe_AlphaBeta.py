# Q1_TicTacToe_AlphaBeta.py
# Tic-Tac-Toe using Alpha–Beta Pruning (Human vs AI)

import math

# Display board
def print_board(board):
    for i in range(3):
        print(board[3*i], board[3*i+1], board[3*i+2])
    print()

# Check winner
def check_winner(board):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),      # rows
        (0,3,6), (1,4,7), (2,5,8),      # cols
        (0,4,8), (2,4,6)                # diagonals
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] != "_":
            return board[a]
    return None

# Check if board full
def is_full(board):
    return "_" not in board

# Alpha-Beta Minimax
def minimax(board, depth, is_max, alpha, beta):
    winner = check_winner(board)
    if winner == "O":   # AI wins
        return 1
    if winner == "X":   # Human wins
        return -1
    if is_full(board):
        return 0        # draw

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == "_":
                board[i] = "O"
                val = minimax(board, depth+1, False, alpha, beta)
                board[i] = "_"
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == "_":
                board[i] = "X"
                val = minimax(board, depth+1, True, alpha, beta)
                board[i] = "_"
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

# Best move for AI
def best_move(board):
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == "_":
            board[i] = "O"
            val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = "_"
            if val > best_val:
                best_val = val
                move = i
    return move

# ------------ MAIN GAME LOOP ------------
board = ["_"] * 9
print("TIC-TAC-TOE (You = X, AI = O)\n")

print_board(board)

while True:
    # Human move
    human = int(input("Enter your move (0-8): "))
    if board[human] != "_":
        print("Invalid! Spot already taken.\n")
        continue
    board[human] = "X"
    print_board(board)

    if check_winner(board) == "X":
        print("You WIN!")
        break
    if is_full(board):
        print("DRAW!")
        break

    # AI move
    print("AI is thinking...\n")
    ai = best_move(board)
    board[ai] = "O"
    print_board(board)

    if check_winner(board) == "O":
        print("AI WINS!")
        break
    if is_full(board):
        print("DRAW!")
        break
