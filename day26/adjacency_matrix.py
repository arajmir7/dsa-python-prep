class GraphMatrix:
    def __init__(self, v):
        self.v = v
        self.graph = [[0]*v for _ in range(v)]

    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1   

    def printGraph(self):
        for row in self.graph:
            print(row)


g = GraphMatrix(4)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)

print("\nAdjacency Matrix:")
g.printGraph()