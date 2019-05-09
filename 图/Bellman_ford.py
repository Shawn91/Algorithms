"""从 start_v 开始，找到它到图内其他任意 vertex 的最短路径
字典 dist: 记录任意 vertex 到 start_v 的距离
字典 pred: 记录任意 vertex 所属最短路径上的上一个 vertex
"""

from math import inf
from graph import Vertex, Graph

def bellman_ford(g, start_v):
    # 初始化
    dist = {v: inf for v in g.getVertices()}
    pred = {v: None for v in g.getVertices()}

    # 设置起点
    dist[start_v] = 0

    # 开始遍历
    for i in range(len(g.getVertices())):
        # 每一轮便利所有的 edges
        for (u,v,weight) in g.getEdges():
            new_distance = dist[u] + weight # new distance for v
            if new_distance < dist[v]: # new distance 小于 v 上一轮设置的到起点的距离
                if i == len(g.getVertices()) - 1: # 执行到第最后一轮时，仍然可以减少 distance，说明存在 weight 和为负的 cycle
                    print('negative cycle exists')
                    return
                dist[v] = new_distance
                pred[v] = u

    return {'pred':pred, 'dist':dist}

if __name__ == '__main__':
    g = Graph(directed=True)
    g.addEdge(0,4,2)
    g.addEdge(4,3,4)
    g.addEdge(4,1,5)
    g.addEdge(1,3,-2)
    g.addEdge(3,2,6)
    g.addEdge(2,1,-3)
    print(bellman_ford(g, 0))




