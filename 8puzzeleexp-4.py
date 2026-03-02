import heapq

GOAL = "12345678e"

INITIAL = "1e2634758"

goal_positions = {}
for i, value in enumerate(GOAL):
    goal_positions[value] = (i // 3, i % 3)


def heuristic(state):
    distance = 0
    for i, value in enumerate(state):
        row, col = i // 3, i % 3
        goal_row, goal_col = goal_positions[value]
        distance += abs(row - goal_row) + abs(col - goal_col)
    return distance


def get_neighbors(state):
    neighbors = []
    index = state.index('e')
    row, col = index // 3, index % 3

    moves = []
    if row > 0: moves.append((-1, 0))
    if row < 2: moves.append((1, 0))
    if col > 0: moves.append((0, -1))
    if col < 2: moves.append((0, 1))

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        new_index = new_row * 3 + new_col
        new_state = list(state)
        new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
        neighbors.append(("".join(new_state), state[new_index]))

    return neighbors


def astar(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL:
            return path + [(None, state)]

        if state in visited:
            continue
        visited.add(state)

        for neighbor, action in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + heuristic(neighbor),
                     g + 1,
                     neighbor,
                     path + [(action, state)])
                )


result = astar(INITIAL)

for i, (action, state) in enumerate(result):
    print()
    if action is None:
        print("Goal achieved!")
    elif i == 0:
        print("Initial configuration")
    else:
        print("After moving", action, "into the empty space")
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
