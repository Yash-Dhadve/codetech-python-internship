# Q2_BFS_InputBased.py
# Breadth First Search (BFS) for directed graph (Input-based)
# Initial node = 1, Goal node = 8

from collections import deque

def bfs(graph, start, goal):
    visited = set([start])
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        order.append(node)

        if node == goal:
            return order

        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

    return order


# -------- USER INPUT SECTION --------
nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))

graph = {i: [] for i in range(1, nodes + 1)}

print("Enter each directed edge as u v:")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)

# Sort adjacency lists for deterministic BFS order
for k in graph:
    graph[k].sort()

start = 1
goal = 8

print(f"\nBFS traversal from node {start} (stops at goal {goal}):")
order = bfs(graph, start, goal)
print(" ".join(map(str, order)))

if order and order[-1] == goal:
    print("Goal node reached:", goal)
else:
    print("Goal node NOT reached.")


"""
Enter number of nodes: 8
Enter number of edges: 11
Enter each directed edge as u v:
1 2
1 4
4 2
2 3
3 4
3 5
3 6
5 7
5 8
6 8
7 8
Enter starting node: 1

BFS traversal from node 1 (stops at goal 8):
1 2 4 6 3 8
Goal node reached: 8
"""
