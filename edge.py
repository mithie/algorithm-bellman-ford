class Edge(object):

    def __init__(self, startVertex, targetVertex, weight):
        self.startVertex=startVertex
        self.targetVertex=targetVertex
        self.weight=weight

    def __repr__(self):
        return repr("{from: " + str(self.startVertex) +  ", to: " + str(self.targetVertex) + ", weight: " + str(self.weight) + "}")
