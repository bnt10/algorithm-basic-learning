# graph 인접행렬
"""
given :
  정점  (A, B, C, D) 
  무방향 간선 [(0,1),(0,2),(0,3),(2,3)
  주어졌을때
  
when :
  graph = adjacencyMatrix()
  graph.setVertex('A')
  graph.setVertex('B')
  graph.setVertex('C')
  graph.setVertex('D')
    
  graph.insertUndirectedEdge(0, 1)
  graph.insertUndirectedEdge(0, 2)
  graph.insertUndirectedEdge(0, 3)
  graph.insertUndirectedEdge(2, 3)
  
then :    
  출력이 다음과 같아야 한다.
       A B C D 

  A :  0 1 1 1 
  
  B :  1 0 0 0 
  
  C :  1 0 0 1 
  
  D :  1 0 1 0  

"""


class AdjacencyMatrix:

    def __init__(self):
        self.MAX_VTXS = 256
        self.size = 0
        self.vertices = []
        self.adjMatrix = []

    def getVertex(self, i):
        return self.vertices[i]

    def setVertex(self, node):
        if self.size > self.MAX_VTXS:
            return
        self.vertices.append(node)
        self.size = self.size + 1

    def getEdge(self, m, n):
        return self.adjMatrix[m][n]

    def setEdge(self, m, n, value):
        try:
            self.adjMatrix[m][n] = value
        except:
            self.adjMatrix.append([0 for i in range(len(self.vertices))])
            self.adjMatrix[m][n] = value

        try:
            self.adjMatrix[n][m] = value
        except:
            self.adjMatrix.append([0 for i in range(len(self.vertices))])
            self.adjMatrix[n][m] = value

    def insertUndirectedEdge(self, m, n):
        self.setEdge(m, n, 1)
        self.setEdge(n, m, 1)

    def drawGraph(self):
        print('    ', end=' ')
        for i in range(self.size):
            print(self.getVertex(i), end=' ')

        for i in range(self.size):
            print('\n')
            print(self.getVertex(i), ': ', end=' ')
            for j in range(self.size):
                print(self.getEdge(i, j), end=' ')
        print('\n')


#정점 삽입 (A, B, C, D)
graph = AdjacencyMatrix()
graph.setVertex('A')
graph.setVertex('B')
graph.setVertex('C')
graph.setVertex('D')

graph.insertUndirectedEdge(0, 1)
graph.insertUndirectedEdge(0, 2)
graph.insertUndirectedEdge(0, 3)
graph.insertUndirectedEdge(2, 3)

graph.drawGraph()
