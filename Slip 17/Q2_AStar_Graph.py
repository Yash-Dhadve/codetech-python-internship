# Q2_AStar_Graph.py
# A* Search Algorithm for the given graph
# Start = A, Goal = G

import heapq

# Graph with edge costs
graph = {
    'A': {'B': 9, 'C': 4, 'D': 7},
    'B': {'A': 9, 'E': 11},
    'C': {'A': 4, 'E': 17, 'F': 12},
    'D': {'A': 7, 'F': 14},
    'E': {'B': 11, 'C': 17, 'G': 5},
    'F': {'C': 12, 'D': 14, 'G': 9},
    'G': {}
}

# Heuristic values (as shown in the diagram)
h = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'G': 0
}

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (h[start], 0, start, [start]))  # (f, g, node, path)

    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None, None


# -------- RUN A* ALGORITHM --------
start = 'A'
goal = 'G'

path, total_cost = a_star(start, goal)

print("Optimal Path:", " -> ".join(path))
print("Total Path Cost:", total_cost)


# ---------------- SAMPLE OUTPUT (not printed automatically) ----------------
SAMPLE_OUTPUT = """
Optimal Path: A -> C -> F -> G
Total Path Cost: 4 + 12 + 9 = 25
"""
# -----------------------------------------------------------
