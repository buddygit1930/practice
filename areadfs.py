# Function to perform DFS
def dfs(graph, start, visited, traversal):
    visited[start] = True
    traversal.append(start)
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited, traversal)

# Main program
n = int(input("Enter number of locations (nodes): "))

# Create adjacency matrix
graph = []
print("\nEnter adjacency matrix (use 1 if route exists, else 0):")
for i in range(n):
    row = list(map(int, input(f"Row {i}: ").split()))
    graph.append(row)

print("\nAdjacency Matrix:")
for row in graph:
    print(row)

start = int(input("\nEnter starting location (node): "))

visited = [False] * n
traversal = []

dfs(graph, start, visited, traversal)

print("\nDFS Traversal sequence:")
print(traversal)
