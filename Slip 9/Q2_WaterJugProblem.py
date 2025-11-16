# Q2_WaterJugProblem.py
# Solve Water Jug Problem using BFS
# Jug A = 5 gallons, Jug B = 7 gallons
# Goal: 4 gallons in Jug B

from collections import deque

# Jug capacities
A = 5
B = 7
GOAL = 4

# BFS function
def water_jug_bfs():
    visited = set()
    q = deque()

    # State represented as (a, b)
    start = (0, 0)
    q.append((start, []))
    visited.add(start)

    while q:
        (a, b), path = q.popleft()

        if b == GOAL:
            return path + [(a, b)]

        # Possible operations
        operations = []

        # 1. Fill jug A
        operations.append((A, b))
        # 2. Fill jug B
        operations.append((a, B))
        # 3. Empty jug A
        operations.append((0, b))
        # 4. Empty jug B
        operations.append((a, 0))
        # 5. Pour A → B
        pour = min(a, B - b)
        operations.append((a - pour, b + pour))
        # 6. Pour B → A
        pour = min(b, A - a)
        operations.append((a + pour, b - pour))

        for state in operations:
            if state not in visited:
                visited.add(state)
                q.append((state, path + [(a, b)]))

    return None


# -------- RUN THE SOLVER --------
solution = water_jug_bfs()

print("Solution steps:\n")
for a, b in solution:
    print(f"Jug A: {a} gallons, Jug B: {b} gallons")


