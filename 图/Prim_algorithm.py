"""
字典 dist: 记录每个 vertex 与已经构建好的部分 tree 中所有节点的距离的最小值
字典 pred: 记录在构建 minimum spanning tree 内，每个 vertex 的父节点
"""

import heapq
import random
from math import inf
from graph import Vertex, Graph

def heapq_decrease(h, item, new_priority):
    """Decrease an item's priority by first deleting it from the heapq and then pushing it back with new priority"""
    h = [x for x in h if x[1]!=item]
    heapq.heappush(h, (new_priority, item))
    return h

def heapq_contains_item(h, item):
    return any([item==e[1] for e in h])

def prim(g):
    # 初始化
    dist = {v:inf for v in g.getVertices()}
    pred = {v:None for v in g.getVertices()}
    pq = []

    # 随机获取第一个元素，并将所有元素插入 pq
    u = random.choice(list(g.getVertices()))
    dist[u] = 0
    for v in g.getVertices():
        heapq.heappush(pq, (dist[v], v))

    # 开始构建 minimum spanning tree
    while pq:
        # u 是最新加入到正在构建中的 minimum spanning tree 的节点；
        _, u = heapq.heappop(pq)
        for adjacent_vertex in g.getVertex(u).getConnections():
            if heapq_contains_item(pq, adjacent_vertex): # 只考虑还在 pq 中的 vertex
                weight = g.getVertex(u).getWeight(g.getVertex(adjacent_vertex))
                if weight < dist[adjacent_vertex]:
                    dist[adjacent_vertex] = weight
                    pred[adjacent_vertex] = u
                    pq = heapq_decrease(pq, adjacent_vertex, weight)

    return {'pred':pred, 'dist':dist}

if __name__ == '__main__':
    g = Graph(directed=False)
    g.addEdge(0,1,2)
    g.addEdge(0,4,4)
    g.addEdge(0,3,8)
    g.addEdge(1,2,3)
    g.addEdge(2,4,1)
    g.addEdge(2,3,5)
    g.addEdge(3,4,7)
    print(prim(g))