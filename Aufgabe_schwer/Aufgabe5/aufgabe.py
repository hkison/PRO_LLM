INF = float('inf')

def floyd_warshall(V, edges):
    # Initialize distance matrix
    dist = [[INF] * V for _ in range(V)]
    
    # Distance from a node to itself is 0
    for i in range(V):
        dist[i][i] = 0
    
    # Add edges to the distance matrix
    for u, v, w in edges:
        dist[u-1][v-1] = w
    
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_solution(dist):
    V = len(dist)
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

if __name__ == "__main__":
    # Example input
    V = 4
    edges = [
        (1, 2, 5),
        (2, 3, 2),
        (3, 4, 3),
        (4, 1, 1)
    ]
    
    dist = floyd_warshall(V, edges)
    print_solution(dist)