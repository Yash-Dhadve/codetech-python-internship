# Q2_BFS_InputBased.py
# Breadth First Search (BFS) program - Input based
# Initial node = 1, Goal node = 7

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

# For undirected graph (as shown in diagram)
graph = {i: [] for i in range(1, nodes + 1)}

print("Enter each edge as u v (undirected):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Sort adjacency lists
for k in graph:
    graph[k].sort()

start = 1
goal = 7

print(f"\nBFS traversal from node {start}:")
order = bfs(graph, start, goal)
print(" ".join(map(str, order)))

if order[-1] == goal:
    print("Goal node reached:", goal)
else:
    print("Goal NOT reached.")
    

"""
Enter number of nodes: 7
Enter number of edges: 9
Enter each edge as u v (undirected):
1 2
1 3
1 4
2 4
2 5
5 6
5 7
4 7
6 7

BFS traversal from node 1:
"""