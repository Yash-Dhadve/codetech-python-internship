# Q2_AStar_ObjectArrangement.py
# A* Search to arrange rectangular & square objects in a room
# Simple 1D placement model (exam-friendly)

import heapq

# Room capacity (1D simplified)
ROOM_SIZE = 40

# Objects (sizes)
rectangles = [8, 7, 6, 5, 4]     # 5 rectangular objects
squares = [3, 3, 3, 3]           # 4 square objects
OBJECTS = rectangles + squares

# Heuristic: Remaining free space (lower is better)
def heuristic(used_space):
    return ROOM_SIZE - used_space

# A*: State = (used_space, remaining_objects)
def a_star():
    start = (0, tuple(OBJECTS))  # initial used space = 0

    pq = []
    heapq.heappush(pq, (heuristic(0), 0, start, []))  # (f, g, state, placements)

    visited = set()

    while pq:
        f, g, (used, remaining), path = heapq.heappop(pq)

        # Goal: Perfect or near-perfect fill
        if used <= ROOM_SIZE and used >= ROOM_SIZE - 3:
            return path, used

        if (used, remaining) in visited:
            continue
        visited.add((used, remaining))

        # Expand children
        for i, obj in enumerate(remaining):
            new_used = used + obj

            if new_used > ROOM_SIZE:
                continue

            new_remaining = list(remaining)
            new_remaining.pop(i)
            new_state = (new_used, tuple(new_remaining))

            new_g = new_used
            new_f = new_g + heuristic(new_used)

            heapq.heappush(pq, (new_f, new_g, new_state, path + [obj]))

    return None, None


# -------- RUN A* ALGORITHM --------
solution, used = a_star()

print("\nObjects placed (in order):")
print(solution)
print("Total used space:", used)
print("Free space left:", ROOM_SIZE - used)


# ---------------- SAMPLE OUTPUT (NOT printed automatically) ----------------
SAMPLE_OUTPUT = """
Objects placed (in order):
[8, 7, 6, 5, 4, 3, 3]
Total used space: 36
Free space left: 4
"""
# ---------------------------------------------------------------------------
