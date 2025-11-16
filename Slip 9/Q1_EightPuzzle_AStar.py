# Q1_EightPuzzle_AStar.py
# Solve 8-Puzzle using A* with Manhattan heuristic
# Prints every intermediate puzzle configuration

import heapq

GOAL = "123456780"   # 0 = blank

# Manhattan Distance heuristic
def manhattan(state):
    h = 0
    for i, val in enumerate(state):
        if val != "0":
            goal_pos = GOAL.index(val)
            h += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return h

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    idx = state.index("0")
    x, y = idx // 3, idx % 3

    moves = {
        "U": (x - 1, y),
        "D": (x + 1, y),
        "L": (x, y - 1),
        "R": (x, y + 1)
    }

    for mv, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx*3 + ny
            s = list(state)
            s[idx], s[new_idx] = s[new_idx], s[idx]
            neighbors.append(("".join(s), mv))

    return neighbors

# A* Algorithm (stores parents for printing path)
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))
    parent = {start: None}
    visited = set()

    while pq:
        _, g, state = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return parent

        for nxt, move in get_neighbors(state):
            if nxt not in visited:
                parent[nxt] = state
                f = g + 1 + manhattan(nxt)
                heapq.heappush(pq, (f, g + 1, nxt))

    return None

# Print puzzle state in 3x3 format
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

# -------- USER INPUT --------
print("Enter initial puzzle state (0 = blank):")
initial = ""
for _ in range(3):
    row = input().split()
    initial += "".join(row)

parent_map = a_star(initial)

if parent_map is None:
    print("No solution found.")
else:
    # Reconstruct full path (reverse)
    path = []
    state = GOAL
    while state is not None:
        path.append(state)
        state = parent_map[state]
    path.reverse()

    print("\nSolution found:\n")
    for st in path:
        print_state(st)


"""
Enter initial puzzle:
1 2 3
4 5 6
7 0 8

Solution found:

1 2 3
4 5 6
7 0 8

1 2 3
4 5 6
7 8 0
"""

