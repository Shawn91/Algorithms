class Vertex:
    def __init__(self, key):
        self.id = key # 每一个 vertex 就是用 id 来表示，给一个不重复的值即可
        self.connectedTo = {} #临近的 vertex 是 key，weight 是value
        
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight # addNeighbor 就是用另一个 vertex 的 id 做 key，weight 做 value 组成的 dict

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f,t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
         return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertList)