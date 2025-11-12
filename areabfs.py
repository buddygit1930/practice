from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal

# Build the graph from user input
graph = {}
n = int(input("Enter number of locations (nodes): "))

print("\nEnter adjacency list (neighbors of each node):")
for i in range(n):
    neighbors = list(map(int, input(f"Enter connected locations for {i} (space-separated): ").split()))
    graph[i] = neighbors

print("\nAdjacency List Representation of Graph:")
for node, edges in graph.items():
    print(f"{node}: {edges}")

start = int(input("\nEnter starting location (node): "))
print("\nBFS Traversal sequence:")
print(bfs(graph, start))
