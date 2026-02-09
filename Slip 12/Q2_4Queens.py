# Q2_4Queens.py
# Solve the 4-Queens problem using simple backtracking
# Prints all distinct solutions for a 4x4 chessboard

def is_safe(positions, row, col):
    """
    Check if a queen can be placed at (row, col).
    positions is a list where index = row and value = column of the queen in that row.
    """
    for r in range(row):
        c = positions[r]
        # same column or same diagonal
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n):
    solutions = []
    positions = [-1] * n  # positions[row] = col

    def backtrack(row):
        if row == n:
            # record a copy of positions
            solutions.append(positions.copy())
            return
        for col in range(n):
            if is_safe(positions, row, col):
                positions[row] = col
                backtrack(row + 1)
                positions[row] = -1  # undo

    backtrack(0)
    return solutions

def print_solution(positions):
    n = len(positions)
    for r in range(n):
        row = []
        for c in range(n):
            row.append("Q" if positions[r] == c else ".")
        print(" ".join(row))
    print()

def main():
    n = 4
    sols = solve_n_queens(n)
    if not sols:
        print("No solutions found.")
        return

    print(f"Number of solutions for {n}-Queens: {len(sols)}\n")
    for idx, sol in enumerate(sols, start=1):
        print(f"Solution {idx}:")
        print_solution(sol)

if __name__ == "__main__":
    main()


# ---------------- SAMPLE OUTPUT (not printed automatically) ----------------
SAMPLE_OUTPUT = """
Number of solutions for 4-Queens: 2

Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .
"""
# ---------------------------------------------------------------------------
