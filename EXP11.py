
n = int(input("Enter number of regions: "))

regions = input("Enter region names: ").split()
colors = input("Enter available colors: ").split()

graph = {}

for region in regions:
    neighbors = input(
        f"Enter neighbors of {region}: "
    ).split()
    graph[region] = neighbors

assigned = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if assigned.get(neighbor) == color:
            return False
    return True

def solve(index):
    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:
        if is_safe(region, color):
            assigned[region] = color

            if solve(index + 1):
                return True

            del assigned[region]

    return False

if solve(0):
    print("\nMap Coloring Solution:")
    for region, color in assigned.items():
        print(region, ":", color)
else:
    print("No solution exists")
