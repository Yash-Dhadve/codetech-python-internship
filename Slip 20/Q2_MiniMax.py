# Q2_MiniMax.py
# Mini-Max Algorithm (Simple Static Game Tree)

# A small game tree (leaf nodes = utility values)
tree = {
    'A': ['B', 'C'],      # Max chooses between B and C
    'B': ['D', 'E'],      # Min chooses between D, E
    'C': ['F', 'G'],      # Min chooses between F, G
    # Leaf nodes:
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}

def minimax(node, isMax):
    # If leaf node → return utility
    if isinstance(tree[node], int):
        return tree[node]

    # MAX player's turn
    if isMax:
        best = -9999
        for child in tree[node]:
            value = minimax(child, False)
            best = max(best, value)
        return best

    # MIN player's turn
    else:
        best = 9999
        for child in tree[node]:
            value = minimax(child, True)
            best = min(best, value)
        return best


# -------- RUN MINIMAX --------
result = minimax('A', True)
print("Optimal value for MAX:", result)


# ---------------- SAMPLE OUTPUT (NOT printed automatically) ----------------
SAMPLE_OUTPUT = """
Mini-Max evaluation:

Leaves:
D=3, E=5 → B = min(3,5) = 3
F=2, G=9 → C = min(2,9) = 2
A = max(B=3, C=2) = 3

Optimal value for MAX: 3
"""
# ---------------------------------------------------------------------------
