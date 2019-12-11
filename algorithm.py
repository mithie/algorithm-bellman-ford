class BellmanFord(object):

    def calculateShortestPath(self, graph, start):
        
        #numVertices = graph.V
        #numEdges = len(graph.edges)

        #print ("numEdges = % d" %(numEdges))

        dist = [float("inf") for x in range(graph.V)]
        dist[start]=0.0

        dist = self.calc(graph, dist, False)

        return self.calc(graph, dist, True)

        #for i in range(0, numVertices-1):
        #    #print("vertex: % d" %(i))
        #    for j in range (numEdges):
        #        #print("    edge: % d" %(j))
        #        for edge in graph.getEdge(j):
        #            #print '        ' + str(type(edge))
        #            minDist = dist[edge.targetVertex]
        #            newDist = dist[edge.startVertex] + edge.weight
        #
        #            if newDist < minDist:
        #                dist[edge.targetVertex] = newDist
        #
        #for i in range(0, numVertices-1):
        #    for j in range (numEdges):
        #        for edge in graph.getEdge(j):
        #
        #            minDist = dist[edge.targetVertex]
        #            newDist = dist[edge.startVertex] + edge.weight
        #
        #            if newDist < minDist:
        #                dist[edge.targetVertex] = float("-inf") 
        #
        #return dist

    def calc(self, graph, dist, calcNegativeCosts):

        numVertices = graph.V
        numEdges = len(graph.edges)

        for i in range(0, numVertices-1):
        #print("vertex: % d" %(i))
            for j in range (numEdges):
                #print("    edge: % d" %(j))
                for edge in graph.getEdge(j):
                    #print '        ' + str(type(edge))
                    minDist = dist[edge.targetVertex]
                    newDist = dist[edge.startVertex] + edge.weight

                    if newDist < minDist:
                        if calcNegativeCosts==True:
                            dist[edge.targetVertex] = float("-inf") 
                        else:
                            dist[edge.targetVertex] = newDist
        
        return dist

