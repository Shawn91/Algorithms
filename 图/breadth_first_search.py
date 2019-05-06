"""从 start_v 开始，遍历整个图，找到 start_v 到其他所有 vertex 的最短路径
字典 dist 用于记录 start_v 到任意 vertex 的最短距离
字典 pred 用于记录任意 vertex 在与 start_v 的最短距离上，之前的一个 vertex 是什么
字段 color 用于记录 vertex 当前的颜色
"""
from queue import Queue
from graph import Vertex, Graph

def bfs(g, start_v):
    vert_queue = Queue()
    # 初始化
    dist = {v:-1 for v in g.getVertices()}
    pred = {v:None for v in g.getVertices()}
    color = {v:'white' for v in g.getVertices()} # 一开始所有的 vertex 的颜色都是 white，表示尚未探索

    color[start_v] = 'gray' # 初始 vertex 首先设为灰色
    dist[start_v] = 0
    vert_queue.put(start_v)
    while not vert_queue.empty():
        current_vert = vert_queue.get()
        for adjacent_vertex in g.getVertex(current_vert).getConnections():
            # 颜色是 white，表示从未访问过；如果是 gray 表示在别的路径上已经访问过该 vertex，不再重复访问
            if color[adjacent_vertex] == 'white':
                vert_queue.put(start_v)
                dist[adjacent_vertex] = dist[current_vert] + 1
                pred[adjacent_vertex] = current_vert
                color[adjacent_vertex] = 'gray'
                vert_queue.put(adjacent_vertex)
        color[current_vert] = 'black' # 当前 vertex 的所有 adjacent vertex 中没有一个是白的
    return {'pred':pred, 'dist':dist, 'color':color}

if __name__ == '__main__':
    g = Graph(directed=False)
    for i in range(9):
        g.addVertex(i)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(3,5)
    g.addEdge(3,6)
    g.addEdge(7,8)

    result = bfs(g, 0)
    pred = result['pred']
    dist = result['dist']
    color = result['color']
    print('pred',pred)
    print('dist',dist)
    print('color',color)