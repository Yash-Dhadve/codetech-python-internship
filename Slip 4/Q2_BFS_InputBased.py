# Q2_BFS_InputBased.py
# Breadth First Search (BFS) program with user input for graph
# Goal node is fixed as 8 (per question)

from collections import deque

def bfs(graph, start, goal):
    visited = set([start])
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        order.append(node)

        if node == goal:
            return order  # stop when goal found

        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

    return order  # goal not found, return full traversal


# -------- USER INPUT SECTION --------
nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))

# create adjacency list for undirected graph (edges added both ways)
graph = {i: [] for i in range(1, nodes + 1)}

print("Enter each edge as two space-separated nodes (u v):")
for _ in range(edges):
    u, v = map(int, input().split())
    # add both directions (treat graph as undirected as per diagram)
    graph[u].append(v)
    graph[v].append(u)

# Make traversal deterministic: sort adjacency lists (ascending)
for k in graph:
    graph[k].sort()

start = int(input("Enter the starting node: "))
goal = 8

print(f"\nBFS traversal from node {start} (stops at goal {goal}):")
traversal = bfs(graph, start, goal)
print(" ".join(map(str, traversal)))

if traversal and traversal[-1] == goal:
    print("Goal node reached:", goal)
else:
    print("Goal node not reached.")
    

"""
Enter number of nodes: 8
Enter number of edges: 10
Enter each edge as two space-separated nodes (u v):
1 2
1 3
2 4
2 5
3 6
3 7
4 8
5 8
6 8
7 8
Enter the starting node: 1

"""

