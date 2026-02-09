# Q2_EightPuzzle_AStar.py
# Solve 8-Puzzle problem using A* Algorithm (Manhattan Distance)

import heapq

GOAL = "123456780"     # 0 = blank tile

# Manhattan distance heuristic
def manhattan(state):
    h = 0
    for i, val in enumerate(state):
        if val != "0":
            goal_pos = GOAL.index(val)
            h += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return h

# Generate legal next states
def get_neighbors(state):
    neighbors = []
    idx = state.index("0")
    x, y = idx // 3, idx % 3

    moves = {
        "U": (x-1, y),
        "D": (x+1, y),
        "L": (x, y-1),
        "R": (x, y+1)
    }

    for mv, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx*3 + ny
            arr = list(state)
            arr[idx], arr[new_idx] = arr[new_idx], arr[idx]
            neighbors.append("".join(arr))

    return neighbors

# A* algorithm
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))
    
    parent = {start: None}
    g_cost = {start: 0}
    visited = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return parent

        for nxt in get_neighbors(state):
            new_g = g_cost[state] + 1

            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                parent[nxt] = state
                new_f = new_g + manhattan(nxt)
                heapq.heappush(pq, (new_f, new_g, nxt))

    return None


# Print puzzle in 3×3 format
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()


# -------- USER INPUT --------
print("Enter initial puzzle state (use 0 for blank):")
initial = ""
for _ in range(3):
    row = input().split()
    initial += "".join(row)

parent_map = a_star(initial)

if parent_map is None:
    print("No solution found.")
else:
    # reconstruct full path
    path = []
    curr = GOAL
    while curr is not None:
        path.append(curr)
        curr = parent_map[curr]
    path.reverse()

    print("\nSolution path:\n")
    for state in path:
        print_board(state)


# ---------------- SAMPLE OUTPUT (NOT printed automatically) ----------------
SAMPLE_OUTPUT = """
Enter initial puzzle:
1 2 3
4 0 6
7 5 8

Solution path:

1 2 3
4 0 6
7 5 8

1 2 3
4 5 6
7 0 8

1 2 3
4 5 6
7 8 0
"""
# ---------------------------------------------------------------------------
