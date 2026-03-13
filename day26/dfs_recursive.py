class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[] for _ in range(v)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)


g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)

visited = [False]*5

print("\nDFS Recursive:")
g.dfs(0, visited)