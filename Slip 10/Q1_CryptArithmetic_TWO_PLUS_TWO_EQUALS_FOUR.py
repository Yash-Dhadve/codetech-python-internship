# Q1_CryptArithmetic_TWO_PLUS_TWO_EQUALS_FOUR.py
# Solve Cryptarithmetic puzzle: TWO + TWO = FOUR

import itertools

# Unique letters in the puzzle
letters = ('T', 'W', 'O', 'F', 'U', 'R')
digits = range(10)

# TWO + TWO = FOUR
def solve():
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if mapping['T'] == 0 or mapping['F'] == 0:
            continue

        T = mapping['T']
        W = mapping['W']
        O = mapping['O']
        F = mapping['F']
        U = mapping['U']
        R = mapping['R']

        # Convert words to numbers
        TWO = 100*T + 10*W + O
        FOUR = 1000*F + 100*O + 10*U + R

        if TWO + TWO == FOUR:
            return mapping, TWO, FOUR

    return None, None, None


# -------- RUN SOLVER --------
solution, TWO_val, FOUR_val = solve()

if solution:
    print("Solution found:\n")
    print("Letter mapping:", solution)
    print(f"TWO  = {TWO_val}")
    print(f"TWO  = {TWO_val}")
    print(f"FOUR = {FOUR_val}")
else:
    print("No solution exists.")


"""
Solution found:

Letter mapping: {'T': 7, 'W': 3, 'O': 2, 'F': 1, 'U': 4, 'R': 6}
TWO  = 732
TWO  = 732
FOUR = 1464
"""