
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter its neighbors separated by spaces: ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph.get(node, []):
            dfs(neighbor, visited)

print("DFS Traversal:")
dfs(start, set())

