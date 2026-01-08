import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start))

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current == goal:
            print("Goal found:", current)
            return

        if current in visited:
            continue

        print("Visited:", current)
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    print("Goal not found")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 6,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

greedy_best_first_search(graph, heuristic, start_node, goal_node)
