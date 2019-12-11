from edge import Edge

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.edges = [[] for i in range(V)]

    def addEdge(self, u, v, w):
        self.edges[u].append(Edge(u, v, w))

    def getEdge(self, u):
        return self.edges[u]

    def containsEdge(self, u, v):
        edge = self.edges[u]
        return (edge.startVertex==u and edge.targetVertex==v)

    def display(self):
        print([str(item) for item in self.edges])
        return ''