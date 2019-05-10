"""输入：directed, weighted graph
字典 dist: 记录任意两个 vertices 之间的距离
字典 pred: 记录任意两个 vertices 之间的最短路径上，key 的上一个 vertex 是什么
"""
from math import inf
from graph import Vertex, Graph

def floyd_warshall(g):
    # 初始化
    dist = {v:{u:inf for u in g.getVertices()} for v in g.getVertices()}
    pred = {v:None for v in g.getVertices()}

    # 将相邻 vertices 之间距离输入 dist 之中
    for (u,v,weight) in g.getEdges():
        dist[u][v] = weight
        dist[u][u] = 0
        dist[v][v] = 0

    # 开始遍历
    for k in g.getVertices():
        for u in g.getVertices():
            for v in g.getVertices():
                new_dist = dist[u][k] + dist[k][v]
                if new_dist < dist[u][v]:
                    dist[u][v] = new_dist
                    pred[v] = u
    return {'pred':pred, 'dist':dist}

if __name__ == '__main__':
    g = Graph(directed=True)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 4, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(2, 4, 1)
    g.addEdge(2, 3, 5)
    g.addEdge(3, 0, 8)
    g.addEdge(4, 3, 7)
    print(floyd_warshall(g))