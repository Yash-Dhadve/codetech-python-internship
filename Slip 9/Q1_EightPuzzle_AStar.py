# Q1_EightPuzzle_AStar.py
# Solve 8-Puzzle using A* algorithm (Manhattan Distance)

import heapq

GOAL = "123456780"      # Goal state, 0 = blank

# Manhattan Distance Heuristic
def manhattan(state):
    dist = 0
    for i, val in enumerate(state):
        if val != "0":
            goal_pos = GOAL.index(val)
            dist += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return dist

# Generate next states
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

    for move, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx*3 + ny
            s_list = list(state)
            s_list[idx], s_list[new_idx] = s_list[new_idx], s_list[idx]
            neighbors.append(("".join(s_list), move))

    return neighbors

# A* Algorithm
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, ""))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return path, g

        for nxt, move in get_neighbors(state):
            if nxt not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(nxt)
                heapq.heappush(pq, (new_f, new_g, nxt, path + move))

    return None, None


# -------- USER INPUT --------
print("Enter initial 8-puzzle state (use 0 for blank):")
initial = ""
for i in range(3):
    row = input().split()
    initial += "".join(row)

print("\nSolving puzzle using A*...\n")
path, cost = a_star(initial)

if path is None:
    print("No solution found.")
else:
    print("Solution (sequence of moves):", path)
    print("Number of moves:", cost)


"""
Enter initial 8-puzzle state (0 = blank):
1 2 3
4 0 6
7 5 8

Solving puzzle using A*...

Solution (sequence of moves): DR
Number of moves: 2
"""
