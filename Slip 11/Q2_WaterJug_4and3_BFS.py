# Q2_WaterJug_4and3_BFS.py
# Solve Water Jug Problem using BFS
# JUG A = 4 gallons, JUG B = 3 gallons
# Goal: 2 gallons in Jug B

from collections import deque

A = 4   # capacity of jug A
B = 3   # capacity of jug B
GOAL = 2

def water_jug_bfs():
    visited = set()
    q = deque()

    start = (0, 0)   # both jugs empty
    q.append((start, []))
    visited.add(start)

    while q:
        (a, b), path = q.popleft()

        # goal condition: Jug B has 2 gallons
        if b == GOAL:
            return path + [(a, b)]

        # List all possible next states
        ops = []

        # 1. Fill jug A completely
        ops.append((A, b))

        # 2. Fill jug B completely
        ops.append((a, B))

        # 3. Empty jug A
        ops.append((0, b))

        # 4. Empty jug B
        ops.append((a, 0))

        # 5. Pour A → B
        pour = min(a, B - b)
        ops.append((a - pour, b + pour))

        # 6. Pour B → A
        pour = min(b, A - a)
        ops.append((a + pour, b - pour))

        # Add new states
        for st in ops:
            if st not in visited:
                visited.add(st)
                q.append((st, path + [(a, b)]))

    return None


# -------- RUN SOLVER --------
solution = water_jug_bfs()

print("Solution steps:\n")
for a, b in solution:
    print(f"Jug A: {a} gallons, Jug B: {b} gallons")



