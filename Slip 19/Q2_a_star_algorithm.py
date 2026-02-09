# A* Search Algorithm Program
# Graph taken from the given diagram

# Heuristic values (h(n))
heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'F': 0
}

# Graph with cost of edges
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('F', 9)],
    'C': [('B', 1)],
    'E': [('A', 3), ('D', 6)],
    'D': [('E', 6), ('F', 1)],
    'F': [('B', 9), ('D', 1)]   # goal node
}

# A* search implementation
def a_star(start, goal):
    open_set = set([start])
    closed_set = set()

    # g(n): cost from start to current node
    g = {start: 0}

    # parent dictionary to reconstruct path
    parent = {start: start}

    while open_set:
        # node with minimum f(n) = g(n) + h(n)
        current = min(open_set, key=lambda node: g[node] + heuristic[node])

        if current == goal:
            # Reconstruct path
            path = []
            while parent[current] != current:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, g[goal]

        open_set.remove(current)
        closed_set.add(current)

        for (neighbor, cost) in graph[current]:
            if neighbor in closed_set:
                continue

            new_g = g[current] + cost

            if neighbor not in open_set or new_g < g.get(neighbor, float('inf')):
                g[neighbor] = new_g
                parent[neighbor] = current
                open_set.add(neighbor)

    return None, None


# -------------------------
# Run A* from A to F
# -------------------------
start_node = 'A'
goal_node = 'F'

path, total_cost = a_star(start_node, goal_node)

print("A* Search Result:")
print("Path found:", path)
print("Total cost:", total_cost)
