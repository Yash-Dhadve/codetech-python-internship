# Q2_DFS_InputBased.py
# Depth First Search (DFS) Program - Input Based
# Initial node = 2, Goal node = 7

def dfs(graph, node, goal, visited):
    print(node, end=" ")
    visited.add(node)

    if node == goal:
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):
                return True
    return False


# -------- USER INPUT SECTION --------
nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))

graph = {i: [] for i in range(1, nodes + 1)}

print("Enter each directed edge as u v:")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)

# Sort adjacency so traversal is deterministic (ascending)
for k in graph:
    graph[k].sort()

# ------------------------------------

start = 2
goal = 7

print(f"\nDFS traversal from node {start}:")
visited = set()
dfs(graph, start, goal, visited)

print("\nGoal node reached:", goal)


"""
Enter number of nodes: 7
Enter number of edges: 10
Enter each directed edge as u v:
1 2
1 3
1 4
2 5
2 4
3 4
4 7
5 6
5 7
6 7

DFS traversal from node 2:

"""

