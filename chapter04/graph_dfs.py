'''
given:
  6개 vertex(정점)과 (0,1), (0,2), (0, 3), (1, 2),(1, 3),(1, 4),(2, 0),(2, 4),(3, 0),
  (4, 1),(4, 5),(5, 2),(5, 4) 간선(edge)가 주어졌을때

when:
  V = 6
  bfsGraph = BfsWithAdjList(V)
  bfsGraph.addEdge(0, 2)
  bfsGraph.addEdge(0, 3)
  bfsGraph.addEdge(1, 2)
  bfsGraph.addEdge(1, 3)
  bfsGraph.addEdge(1, 4)
  bfsGraph.addEdge(2, 0)
  bfsGraph.addEdge(2, 4)
  bfsGraph.addEdge(3, 0)
  bfsGraph.addEdge(4, 1)
  bfsGraph.addEdge(4, 5)
  bfsGraph.addEdge(5, 2)
  bfsGraph.addEdge(5, 4)
  print(bfsGraph.display(1))
  
then:
 [1, 4, 5, 2, 0, 3]
'''

class BfsWithAdjList():

    def __init__(self, V):
        self.vertex = V
        self.graph = [[] for i in  range(self.vertex)]

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
bfsGraph = BfsWithAdjList(V)
bfsGraph.addEdge(0, 2)
bfsGraph.addEdge(0, 3)
bfsGraph.addEdge(1, 2)
bfsGraph.addEdge(1, 3)
bfsGraph.addEdge(1, 4)
bfsGraph.addEdge(2, 0)
bfsGraph.addEdge(2, 4)
bfsGraph.addEdge(3, 0)
bfsGraph.addEdge(4, 1)
bfsGraph.addEdge(4, 5)
bfsGraph.addEdge(5, 2)
bfsGraph.addEdge(5, 4)
print(bfsGraph.display(1))

