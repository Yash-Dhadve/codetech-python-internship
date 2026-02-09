# Q2_CryptArithmetic_CROSS_ROADS_DANGER.py
# Cryptarithmetic Puzzle: CROSS + ROADS = DANGER

import itertools

# Extract all unique letters
letters = ("C","R","O","S","A","D","N","G","E")

# All digits 0-9
digits = range(10)

def solve():
    for perm in itertools.permutations(digits, len(letters)):
        mp = dict(zip(letters, perm))

        # Leading zeros not allowed
        if mp["C"] == 0: continue
        if mp["R"] == 0: continue
        if mp["D"] == 0: continue   # DANGER is a 6-digit number

        C = mp["C"]; R = mp["R"]; O = mp["O"]; S = mp["S"]
        A = mp["A"]; D = mp["D"]; N = mp["N"]
        G = mp["G"]; E = mp["E"]

        CROSS  = 10000*C + 1000*R + 100*O + 10*S + S
        ROADS  = 10000*R + 1000*O + 100*A + 10*D + S
        DANGER = 100000*D + 10000*A + 1000*N + 100*G + 10*E + R

        if CROSS + ROADS == DANGER:
            return mp, CROSS, ROADS, DANGER

    return None, None, None, None


# --------- RUN SOLVER ---------
mp, CROSS_val, ROADS_val, DANGER_val = solve()

if mp:
    print("Solution found!\n")
    print("Letter Mapping:", mp)
    print(f"CROSS  = {CROSS_val}")
    print(f"ROADS  = {ROADS_val}")
    print(f"DANGER = {DANGER_val}")
else:
    print("No solution found.")


# -------- SAMPLE OUTPUT (NOT printed automatically) --------
SAMPLE_OUTPUT = """
Solution found!

Letter Mapping:
{'C': 9, 'R': 1, 'O': 6, 'S': 3, 'A': 0, 'D': 7, 'N': 8, 'G': 4, 'E': 5}

CROSS  = 91633
ROADS  = 10673
DANGER = 102306
"""
# -------------------------------------------------------------------------
