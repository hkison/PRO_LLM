from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.capacity = {}

    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0

    def bfs(self, s, t, parent):
        visited = [False] * (self.V)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind in self.graph[u]:
                if visited[ind] == False and self.capacity[(u, ind)] > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.V)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow

if __name__ == "__main__":
    V, E = map(int, input().split())
    s, t = map(int, input().split())
    graph = Graph(V + 1)

    for _ in range(E):
        u, v, c = map(int, input().split())
        graph.add_edge(u, v, c)

    print(graph.ford_fulkerson(s, t))