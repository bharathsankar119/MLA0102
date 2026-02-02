from collections import deque

def water_jug():
    # capacities
    jug1 = 4
    jug2 = 3

    # initial state (0,0)
    start = (0, 0)
    goal = (2, 0)

    queue = deque([start])
    visited = set()
    visited.add(start)

    print("Steps:")

    while queue:
        x, y = queue.popleft()
        print((x, y))

        if (x, y) == goal:
            print("Goal reached!")
            return

        # all possible operations
        states = [
            (jug1, y),                 # Fill Jug1
            (x, jug2),                 # Fill Jug2
            (0, y),                    # Empty Jug1
            (x, 0),                    # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 -> Jug1
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("Goal not possible")

# run
water_jug()
