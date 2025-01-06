import heapq

# Dijkstra's algorithm implementation
def dijkstra(V, edges, start):
    graph = {i: [] for i in range(1, V + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))

    distances = {i: float('inf') for i in range(1, V + 1)}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return [distances[i] if distances[i] != float('inf') else 'INF' for i in range(1, V + 1)]

# Given input
V = 5
E = 6
start_node = 1
edges = [
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 1),
    (2, 4, 2),
    (3, 5, 3),
    (4, 5, 1)
]

# Run the function and print the result
result = dijkstra(V, edges, start_node)
print(result)
