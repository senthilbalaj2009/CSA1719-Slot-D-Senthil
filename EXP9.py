
from itertools import permutations

n = int(input("Enter number of cities: "))

dist = []
for i in range(n):
    row = list(map(int, input(
        f"Enter distances from city {i}: ").split()))
    dist.append(row)

start = int(input("Enter starting city (0 to n-1): "))

cities = [i for i in range(n) if i != start]
min_cost = float('inf')
best_path = []

for p in permutations(cities):
    path = [start] + list(p) + [start]
    cost = 0

    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Shortest path:", " -> ".join(map(str, best_path)))
print("Minimum cost:", min_cost)
