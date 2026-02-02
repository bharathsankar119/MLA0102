def ucs(graph, start, goal):
    visited = []
    queue = [(0, start)]   # (cost, node)

    print("UCS Traversal:", end=" ")

    while queue:
        # sort based on cost
        queue.sort()
        cost, node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == goal:
                print("\nGoal reached with cost:", cost)
                return

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((cost + weight, neighbor))

    print("\nGoal not reachable")

# -------- Input inside the code --------
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
goal_node = 'D'

ucs(graph, start_node, goal_node)
