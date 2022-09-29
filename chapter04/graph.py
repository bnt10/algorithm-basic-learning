# graph 인접행렬


class adjacencyMatrix:

    def __init__(self):
        self.MAX_VTXS = 256
        self.size = 0
        self.vertices = []
        self.adjMatrix = []

    def getVertex(self, i):
        return self.__vertices[i]

    def setVertex(self, node):
        if self.size > self.MAX_VTXS:
            return
        print(self.size)
        self.vertices.append(node)
        self.size = self.size + 1

    def getEdge(self, m, n):
        return self.adjMatrix[m][n]

    def setEdge(self, m, n, value):
        self.adjMatrix.append([m,n])
        print(self.adjMatrix)
    def reset(self):
        for m in range(self.MAX_VTXS):
            for n in range(self.MAX_VTXS):
                print(m, n)
                self.setEdge = (m, n, 0)
        self.size = 0

    def insertUndirectedEdge(self, m, n):
        self.setEdge(m, n, 1)
        self.setEdge(n, m, 1)

    def calculate(self):
        print('vertex szie', self.size)
        # print('------')
        # for i in self.size:
        #     print(self.getVertex(i))

        # for i in self.size:
        #     print(self.getVertex(i), ': ')
        #     for j in self.size:
        #         print(self.getVertex(i, j), ': ')


#정점 삽입 (A, B, C, D)
graph = adjacencyMatrix()
graph.setVertex('A')
graph.setVertex('B')
graph.setVertex('C')
graph.setVertex('D')

graph.insertUndirectedEdge(0, 1)
graph.insertUndirectedEdge(0, 2)
graph.insertUndirectedEdge(0, 3)
graph.insertUndirectedEdge(2, 3)

graph.calculate()
