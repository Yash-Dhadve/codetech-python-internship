# Q1_MiniMaxAlgorithm.py
# Simple implementation of Mini-Max Algorithm
# Using a static game tree for demonstration

def minimax(depth, node_index, is_max, scores, height):
    # If leaf node reached, return score
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )


# -------- SAMPLE GAME TREE --------
# Tree depth = 3, leaves = 8
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Log base 2 of number of leaves = height of tree
import math
height = int(math.log2(len(scores)))

print("Mini-Max result:", minimax(0, 0, True, scores, height))


"""
Given leaf node values:
[3, 5, 2, 9, 12, 5, 23, 23]

Mini-Max result: 12
"""
