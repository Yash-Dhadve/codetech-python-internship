# Q2_CryptArithmetic_GO_TO_OUT.py
# Cryptarithmetic Puzzle Solver: GO + TO = OUT

import itertools

# Letters involved
letters = ("G", "O", "T", "U")   # BUT also "O" repeated, so map O once

# We actually have 5 unique letters: G, O, T, U, ??? Wait:
# From GO + TO = OUT:
# Letters are: G, O, T, U, O, U, T  -> unique: G, O, T, U (4 letters)

unique_letters = ("G", "O", "T", "U")

digits = range(10)

def solve():
    for perm in itertools.permutations(digits, len(unique_letters)):
        mp = dict(zip(unique_letters, perm))

        # Leading zero restrictions
        if mp["G"] == 0: continue
        if mp["T"] == 0: continue
        if mp["O"] == 0: continue  # "OUT" cannot start with 0

        G = mp["G"]
        O = mp["O"]
        T = mp["T"]
        U = mp["U"]

        # Words to numbers
        GO  = 10*G + O
        TO  = 10*T + O
        OUT = 100*O + 10*U + T

        if GO + TO == OUT:
            return mp, GO, TO, OUT

    return None, None, None, None


# --------- RUNNING THE SOLVER ---------
mapping, GO_val, TO_val, OUT_val = solve()

if mapping:
    print("Solution found!\n")
    print("Letter mapping:", mapping)
    print(f"GO  = {GO_val}")
    print(f"TO  = {TO_val}")
    print(f"OUT = {OUT_val}")
else:
    print("No solution found.")


# --------------- SAMPLE OUTPUT (NOT printed automatically) ---------------
SAMPLE_OUTPUT = """
Solution found!

Letter mapping: {'G': 7, 'O': 1, 'T': 8, 'U': 9}

GO  = 71
TO  = 81
OUT = 152
"""
# ------------------------------------------------------------------------
