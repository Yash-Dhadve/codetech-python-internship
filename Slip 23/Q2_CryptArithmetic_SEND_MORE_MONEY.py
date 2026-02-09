# Q2_CryptArithmetic_SEND_MORE_MONEY.py
# Cryptarithmetic: SEND + MORE = MONEY

import itertools

# Unique letters in the puzzle
letters = ("S", "E", "N", "D", "M", "O", "R", "Y")

# All 10 digits
digits = range(10)

def solve():
    for perm in itertools.permutations(digits, len(letters)):
        mp = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if mp["S"] == 0: continue
        if mp["M"] == 0: continue

        S = mp["S"]
        E = mp["E"]
        N = mp["N"]
        D = mp["D"]
        M = mp["M"]
        O = mp["O"]
        R = mp["R"]
        Y = mp["Y"]

        SEND  = 1000*S + 100*E + 10*N + D
        MORE  = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        if SEND + MORE == MONEY:
            return mp, SEND, MORE, MONEY

    return None, None, None, None


# -------- RUN SOLVER --------
mapping, SEND_val, MORE_val, MONEY_val = solve()

if mapping:
    print("Solution found!\n")
    print("Letter mapping:", mapping)
    print(f"SEND  = {SEND_val}")
    print(f"MORE  = {MORE_val}")
    print(f"MONEY = {MONEY_val}")
else:
    print("No solution found.")


# ---------------- SAMPLE OUTPUT (not printed automatically) ----------------
SAMPLE_OUTPUT = """
Solution found!

Letter mapping:
{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

SEND  = 9567
MORE  = 1085
MONEY = 10652
"""
# ---------------------------------------------------------------------------
