# graph 인접행렬


class adjacencyMatrix:

    def __init__(self):
        self.__MAX_VTXS = 256
        self.__size = 0
        self.__vertices = []
        self.__adjMatrix = []
        self.reset()

    @property
    def vertex(self, i):
        return self.vertices[i]

    @property
    def edge(self, m, n):
        return self.__adjMatrix[m][n]

    @edge.setter
    def edge(self, m, n, value):
        self.__adjMatrix[m][n] = value

    @vertex.setter
    def vertex(self, node):
        if self.__size > self.__MAX_VTXS:
            return
        self.__size = self.__size + 1
        self.__vertex[self.__size] = node

    def reset(self):
        for m in range(self.__MAX_VTXS):
            for n in range(self.__MAX_VTXS):
                print(m, n)
                self.edge = (0, 0, 0)
        self.__size = 0

    def insertUndirectedEdge(self, m, n):
        self.edge = (m, n, 1)
        self.edge = (n, m, 1)

    def calculate(self):
        print('vertex szie', self.__size)
        print('------')
        for i in self.__size:
            print(self.vertex(i))

        for i in self.__size:
            print(self.vertex(i), ': ')
            for j in self.__size:
                print(self.edge(i, j), ': ')


#정점 삽입 (A, B, C, D)
graph = adjacencyMatrix()
graph.vertex = 'A' // 0
graph.vertex = 'B' // 0
graph.vertex = 'C' // 0
graph.vertex = 'D' // 0

graph.insertUndirectedEdge(0, 1)
graph.insertUndirectedEdge(0, 2)
graph.insertUndirectedEdge(0, 3)
graph.insertUndirectedEdge(2, 3)

graph.calculate()
