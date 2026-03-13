class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[] for _ in range(v)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  

    def printGraph(self):
        for i in range(self.v):
            print(i, "->", self.graph[i])


g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)

print("Adjacency List:")
g.printGraph()