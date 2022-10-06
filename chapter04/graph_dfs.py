'''
given:
  6개 vertex(정점)과 (0,1), (0,2), (0, 3), (1, 2),(1, 3),(1, 4),(2, 0),(2, 4),(3, 0),
  (4, 1),(4, 5),(5, 2),(5, 4) 간선(edge)가 주어졌을때

when:
  V = 6
  dfsGraph = dfsWithAdjList(V)
  dfsGraph.addEdge(0, 2)
  dfsGraph.addEdge(0, 3)
  dfsGraph.addEdge(1, 2)
  dfsGraph.addEdge(1, 3)
  dfsGraph.addEdge(1, 4)
  dfsGraph.addEdge(2, 0)
  dfsGraph.addEdge(2, 4)
  dfsGraph.addEdge(3, 0)
  dfsGraph.addEdge(4, 1)
  dfsGraph.addEdge(4, 5)
  dfsGraph.addEdge(5, 2)
  dfsGraph.addEdge(5, 4)
  print(dfsGraph.display(1))

  
then:
 [1, 4, 5, 2, 0, 3]
'''


class dfsWithAdjList():

    def __init__(self, V):
        self.vertex = V
        self.graph = [[] for i in range(self.vertex)]

    def addEdge(self, source, target):
        self.graph[source].append(target)

    def display(self, startNode):

        visited = []
        stack = [startNode]
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)

                stack += set(self.graph[n]) - set(visited)
        return visited


V = 6
dfsGraph = dfsWithAdjList(V)
dfsGraph.addEdge(0, 1)
dfsGraph.addEdge(0, 2)
dfsGraph.addEdge(0, 3)
[1, 2, 3]
dfsGraph.addEdge(1, 2)
dfsGraph.addEdge(1, 3)
dfsGraph.addEdge(1, 4)
dfsGraph.addEdge(2, 0)
dfsGraph.addEdge(2, 4)
dfsGraph.addEdge(3, 0)
dfsGraph.addEdge(4, 1)
dfsGraph.addEdge(4, 5)
dfsGraph.addEdge(5, 2)
dfsGraph.addEdge(5, 4)
print(dfsGraph.display(0))
