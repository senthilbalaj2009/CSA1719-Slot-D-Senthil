
import heapq

graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    h[node] = int(input("Enter heuristic value: "))
    neighbors = input("Enter neighbors (node cost): ").split()

    graph[node] = {}
    for j in range(0, len(neighbors), 2):
        graph[node][neighbors[j]] = int(neighbors[j + 1])

start = input("Enter start node: ")
goal = input("Enter goal node: ")

pq = [(h[start], 0, start, [start])]
visited = set()

while pq:
    f, g, node, path = heapq.heappop(pq)

    if node == goal:
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", g)
        break

    if node in visited:
        continue
    visited.add(node)

    for neighbor, cost in graph.get(node, {}).items():
        if neighbor not in visited:
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(
                pq, (new_f, new_g, neighbor, path + [neighbor])
            )
else:
    print("No path found")
