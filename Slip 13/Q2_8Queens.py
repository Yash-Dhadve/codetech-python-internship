# Q2_8Queens.py
# Solve 8-Queens problem using simple backtracking

N = 8   # board size

# Check if placing a queen at (row, col) is safe
def is_safe(board, row, col):
    # Check column
    for r in range(row):
        if board[r] == col:
            return False

    # Check diagonal (top-left to bottom-right)
    for r in range(row):
        if abs(board[r] - col) == abs(r - row):
            return False

    return True


# Backtracking function
def solve_queens(row, board, solutions):
    if row == N:
        solutions.append(board.copy())
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(row + 1, board, solutions)
            board[row] = -1  # undo


# Print board nicely
def print_board(board):
    for r in range(N):
        row = []
        for c in range(N):
            if board[r] == c:
                row.append("Q")
            else:
                row.append(".")
        print(" ".join(row))
    print()


# ---------------- MAIN ----------------
solutions = []
board = [-1] * N

solve_queens(0, board, solutions)

print(f"Total solutions for 8-Queens: {len(solutions)}\n")

for i, sol in enumerate(solutions, start=1):
    print(f"Solution {i}:")
    print_board(sol)


