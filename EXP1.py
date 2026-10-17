import heapq

def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)
    return distance

def solve(start, goal):
    pq = [(heuristic(start, goal), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            for step in path:
                print(step[0:3])
                print(step[3:6])
                print(step[6:9])
                print()
            return

        zero = state.index(0)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            x, y = zero // 3 + dx, zero % 3 + dy

            if 0 <= x < 3 and 0 <= y < 3:
                new_zero = x * 3 + y
                new_state = list(state)
                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )
                new_state = tuple(new_state)

                if new_state not in visited:
                    h = heuristic(new_state, goal)
                    heapq.heappush(
                        pq, (g + 1 + h, g + 1, new_state, path)
                    )

    print("No solution found")

start = tuple(map(int, input("Enter initial state (0 for blank): ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))

solve(start, goal)
