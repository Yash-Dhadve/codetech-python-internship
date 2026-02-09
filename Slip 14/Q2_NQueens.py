# Q2_NQueens.py
# Program to simulate N-Queens problem using Backtracking

def is_safe(board, row, col, n):
    # Check column
    for r in range(row):
        if board[r] == col:
            return False

    # Check diagonals
    for r in range(row):
        if abs(board[r] - col) == abs(r - row):
            return False

    return True


def solve_queens(row, board, solutions, n):
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_queens(row + 1, board, solutions, n)
            board[row] = -1   # backtrack


def print_board(board):
    n = len(board)
    for r in range(n):
        row = []
        for c in range(n):
            row.append("Q" if board[r] == c else ".")
        print(" ".join(row))
    print()


# -------------- MAIN --------------
n = int(input("Enter value of N for N-Queens: "))

board = [-1] * n
solutions = []

solve_queens(0, board, solutions, n)

print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")

for i, sol in enumerate(solutions, start=1):
    print(f"Solution {i}:")
    print_board(sol)


