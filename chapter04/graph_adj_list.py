# graph 인접리스트
"""
given:
  3개 vertex(정점)과 (0,1) (0,2) 간선(edge)가 주어졌을때
when:
  V = 3
  graph = AdjacencyList(V)
  graph.addEdge(0, 1)
  graph.addEdge(0, 2)
  graph.drawGraph()
then:
  출력이 다음과 같아야 한다.
  
  vertext:0
  0 -> 2 -> 1 
  
  vertext:1
  1 -> 0 
  
  vertext:2
  2 -> 0 
"""


class AdjacencyList:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def getLinkNode(self, data, pointer):
        return {'data': data, 'pointer': pointer}

    def addEdge(self, source, target):

        self.graph[source] = self.getLinkNode(data=target,
                                              pointer=self.graph[source])
        #if it is an undirected graph.
        self.graph[target] = self.getLinkNode(data=source,
                                              pointer=self.graph[target])

    def drawGraph(self):

        for i in range(self.V):
            print('vertext:{0}\n{0}'.format(i), end="")
            temp = self.graph[i]

            while temp:
                print(" -> {}".format(temp['data']), end="")
                temp = temp['pointer']
            print(' \n')


V = 3
graph = AdjacencyList(V)
graph.addEdge(0, 1)
graph.addEdge(0, 2)

graph.drawGraph()
