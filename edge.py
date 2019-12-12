class Edge(object):

    def __init__(self, startVertex, targetVertex, weight):
        self.startVertex=startVertex
        self.targetVertex=targetVertex
        self.weight=weight

    def __repr__(self):
        return repr("{from: % d, to: % d, weight: % 5.2f}" %(self.startVertex, self.targetVertex, self.weight))
