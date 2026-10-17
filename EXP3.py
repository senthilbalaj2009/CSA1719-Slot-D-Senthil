from collections import deque

def water_jug(a, b, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        print(x, y)

        if x == target or y == target:
            print("Target reached!")
            return

        queue.extend([
            (a, y),
            (x, b),
            (0, y),
            (x, 0),
            (x - min(x, b - y), y + min(x, b - y)),
            (x + min(y, a - x), y - min(y, a - x))
        ])

    print("No solution exists")

a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

water_jug(a, b, target)