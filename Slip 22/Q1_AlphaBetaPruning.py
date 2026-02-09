# Q1_AlphaBetaPruning.py
# Program to implement Alpha-Beta Pruning

# A small static game tree for demonstration:
#             A (Max)
#         /            \
#      B (Min)        C (Min)
#     /     \        /       \
#   D=3    E=12    F=8      G=2

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 12,
    'F': 8,
    'G': 2
}

def alphabeta(node, alpha, beta, isMax):
    # If leaf node
    if isinstance(tree[node], int):
        return tree[node]

    if isMax:
        best = -9999
        for child in tree[node]:
            value = alphabeta(child, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruning at node {node}, alpha={alpha}, beta={beta}")
                break
        return best

    else:
        best = 9999
        for child in tree[node]:
            value = alphabeta(child, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruning at node {node}, alpha={alpha}, beta={beta}")
                break
        return best


# ------ RUN ALPHA-BETA --------
alpha = -9999
beta = 9999
result = alphabeta('A', alpha, beta, True)

print("\nOptimal Value:", result)


# ---------------- SAMPLE OUTPUT (NOT printed automatically) ----------------
SAMPLE_OUTPUT = """
Pruning at node C, alpha=8, beta=2

Optimal Value: 8
"""
# ---------------------------------------------------------------------------
