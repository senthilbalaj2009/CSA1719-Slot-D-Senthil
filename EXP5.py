
from collections import deque

m = int(input("Enter number of missionaries: "))
c = int(input("Enter number of cannibals: "))
capacity = int(input("Enter boat capacity: "))

start = (m, c, 1)
goal = (0, 0, 0)
moves = [(i, j) for i in range(capacity + 1)
         for j in range(capacity + 1)
         if 1 <= i + j <= capacity]

def safe(x, y):
    return (0 <= x <= m and 0 <= y <= c and
            (x == 0 or x >= y) and
            (m - x == 0 or m - x >= c - y))

queue = deque([(start, [start])])
visited = {start}
found = False

while queue:
    state, path = queue.popleft()
    x, y, boat = state

    if state == goal:
        print("\nSolution:")
        for s in path:
            print(s)
        found = True
        break

    for a, b in moves:
        if boat == 1:
            nx, ny, nb = x - a, y - b, 0
        else:
            nx, ny, nb = x + a, y + b, 1

        new = (nx, ny, nb)

        if safe(nx, ny) and new not in visited:
            visited.add(new)
            queue.append((new, path + [new]))

if not found:
    print("No solution exists")
