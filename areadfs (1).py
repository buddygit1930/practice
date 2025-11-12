# Function to perform DFS
def dfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

# Main Program
print("=== DFS Traversal of City Locations (Adjacency Matrix) ===")

n = int(input("Enter number of locations (nodes): "))

# Create adjacency matrix
graph = []
print("\nEnter adjacency matrix (use 1 if route exists, else 0):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Perform DFS starting from node 0
visited = [False] * n
print("\nSequence of visiting locations using DFS (starting from 0):")
dfs(graph, 0, visited)
print()
