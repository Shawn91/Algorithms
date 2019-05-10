"""从 start_v 开始，找到它到图内其他任意 vertex 的最短路径
字典 dist: 记录任意 vertex 到 start_v 的距离
字典 pred: 记录任意 vertex 所属最短路径上的上一个 vertex
"""
import heapq
from math import inf
from graph import Vertex, Graph

def heapq_decrease(h, item, new_priority):
    """Decrease an item's priority by first deleting it from the heapq and then pushing it back with new priority"""
    h = [x for x in h if x[1]!=item]
    heapq.heappush(h, (new_priority, item))
    return h

def dijkstra(g, start_v):
    # 初始化
    dist = {v:inf for v in g.getVertices()}
    pred = {v:None for v in g.getVertices()}
    pq = [] # priority queue

    # 设置起点，并将所有 vertices 加入 pq 中
    dist[start_v] = 0
    for v in g.getVertices():
        heapq.heappush(pq, (dist[v], v))

    while pq:
        current_vertex = heapq.heappop(pq)[1]
        for adjacent_vertex in g.getVertex(current_vertex).getConnections():
            # current_vertex 到 start_v 的距离 + current_vertex与adjacent_vertex 之间距离
            new_distance = dist[current_vertex] + g.getVertex(current_vertex).getWeight(g.getVertex(adjacent_vertex))
            if new_distance < dist[adjacent_vertex]:
                dist[adjacent_vertex] = new_distance
                pred[adjacent_vertex] = current_vertex
                pq = heapq_decrease(pq, adjacent_vertex, new_distance)
    return {'pred':pred, 'dist':dist}

if __name__ == '__main__':
    g = Graph(directed=True)
    g.addEdge(0,1,6)
    g.addEdge(0,2,8)
    g.addEdge(0,3,18)
    g.addEdge(1,4,11)
    g.addEdge(2,3,9)
    g.addEdge(4,5,3)
    g.addEdge(5,3,2)
    g.addEdge(5,2,7)
    print(dijkstra(g,1))