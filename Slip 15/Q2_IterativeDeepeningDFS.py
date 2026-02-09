# Q2_IterativeDeepeningDFS.py
# Implement Iterative Deepening Depth First Search (IDDFS)
# Goal Node = G

# Graph as shown in the diagram
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": [],
    "F": ["K"],
    "G": [],
    "H": [],
    "I": [],
    "K": []
}

# Depth Limited Search (DLS)
def dls(node, goal, depth):
    print(node, end=" ")

    if node == goal:
        return True

    if depth == 0:
        return False

    for child in graph[node]:
        if dls(child, goal, depth - 1):
            return True

    return False


# Iterative Deepening DFS
def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth = {depth}: ", end="")
        if dls(start, goal, depth):
            print("\nGoal Found at depth", depth)
            return
    print("Goal NOT found.")


# -------- RUN IDDFS --------
start = "A"
goal = "G"
max_depth = 5

iddfs(start, goal, max_depth)


# ---------------- SAMPLE OUTPUT (not printed automatically) ----------------
SAMPLE_OUTPUT = """
Depth = 0: A
Depth = 1: A B C
Depth = 2: A B D E C F G
Goal Found at depth 2
"""
# ---------------------------------------------------------------------------
