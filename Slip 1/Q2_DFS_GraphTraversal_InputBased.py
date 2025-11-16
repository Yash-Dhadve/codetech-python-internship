# DFS Program with user input for graph
# Initial node = user input, Goal node = 8

def dfs(graph, node, goal, visited):
    visited.add(node)
    print(node, end=" ")

    if node == goal:
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):
                return True
    return False


# --------- User Input Section ----------
nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))

# create adjacency list
graph = {i: [] for i in range(1, nodes + 1)}

print("Enter each edge as two space-separated nodes (u v):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)   # directed graph
# ----------------------------------------

start = int(input("Enter the starting node: "))
goal = 8

print(f"DFS traversal from node {start} :")
visited = set()
dfs(graph, start, goal, visited)

print("\nGoal node reached:", goal)


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