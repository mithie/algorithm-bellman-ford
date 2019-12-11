from algorithm import BellmanFord
from graph import Graph
from edge import Edge

V = 8
graph = Graph(V)


#graph.addEdge(0, 1, 3)
#graph.addEdge(1, 2, 9)
#graph.addEdge(0, 2, 5)
#graph.addEdge(2, 3, 12)


#V = 5
#graph.addEdge(0, 1, -1)
#graph.addEdge(0, 2, 4)
#graph.addEdge(1, 2, 3)
#graph.addEdge(1, 3, 2)
#graph.addEdge(1, 4, 2)
#graph.addEdge(3, 2, 5)
#graph.addEdge(3, 1, 1)
#graph.addEdge(4, 3, -3)


graph.addEdge(0, 1, 1)
graph.addEdge(1, 2, 1)
graph.addEdge(2, 4, 1)
graph.addEdge(4, 3, -3)
graph.addEdge(3, 2, 1)
graph.addEdge(1, 5, 4)
graph.addEdge(1, 6, 4)
graph.addEdge(5, 6, 5)
graph.addEdge(6, 7, 4)
graph.addEdge(5, 7, 3)

#print graph.containsEdge(0,2)

#print graph.display()

#print [str(item) for item in graph.edges]

bellmanFord = BellmanFord()
d = bellmanFord.calculateShortestPath(graph, 0)

for i in range(V):
    print("The cost to get from node % d to % d is: % 5.2f" %(0, i, d[i]))