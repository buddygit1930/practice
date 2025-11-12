from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return order

# Main Program
print("=== BFS Traversal of City Locations ===")
n = int(input("Enter number of locations (nodes): "))

# Create adjacency list
graph = {}
for i in range(n):
    connections = list(map(int, input(f"Enter locations connected to {i}: ").split()))
    graph[i] = connections

# Perform BFS starting from node 0
start = 0
print(f"\nGraph (Adjacency List): {graph}")
bfs_order = bfs(graph, start)
print(f"\nSequence of visiting locations using BFS (starting from {start}): {bfs_order}")
