"""从 start_v 开始，遍历整个图，找到 start_v 到其他所有 vertex 的路径（未必最短）
字典 pred: 记录每个 vertex 在所属 path 上的前一个 vertex 是什么
字段 color: 用于记录 vertex 当前的颜色
字典 encounter_times: 记录每个 vertex 在首次访问时，整个图已经访问了多少步了
字典 finish_times: 记录每个 vertex 在结束访问时（标记为黑色，即所有临近 vertices 都非白色）时，整个图已经访问了多少步了
"""

from graph import Vertex, Graph

class DFS:
    def __init__(self, g, start_v):
        self.g = g
        self.start_v = start_v
        self.steps = 0 # 记录已经走了多少步
        self.pred = {v:None for v in g.getVertices()}
        self.color = {v:'white' for v in g.getVertices()}
        self.encounter_times = {v:0 for v in g.getVertices()}
        self.finish_times = {v:0 for v in g.getVertices()}

        # 访问起始点 start_v
        self.color[self.start_v] = 'gray'
        self.steps += 1
        self.encounter_times[self.start_v] = self.steps
        self.dfs_search(self.start_v)

    def dfs_search(self, v):
        for adjacent_vertex in self.g.getVertex(v).getConnections():
            if self.color[adjacent_vertex] == 'white':
                self.steps += 1
                self.color[adjacent_vertex] = 'gray'
                self.pred[adjacent_vertex] = v
                self.encounter_times[adjacent_vertex] = self.steps
                self.dfs_search(adjacent_vertex)
        self.steps += 1
        self.color[v] = 'black'
        self.finish_times[v] = self.steps


if __name__ == '__main__':
    g = Graph(directed=True)
    for i in ['A','B','C','D','E','F']:
        g.addVertex(i)
    g.addEdge('A', 'B')
    g.addEdge('A', 'D')
    g.addEdge('B', 'C')
    g.addEdge('B', 'D')
    g.addEdge('D', 'E')
    g.addEdge('E', 'B')
    g.addEdge('E', 'F')
    g.addEdge('F', 'C')
    dfs = DFS(g,'A')
    print('pred', dfs.pred)
    print('steps', dfs.steps)
    print('color', dfs.color)
    print('encounter_times', dfs.encounter_times)
    print('finish_times', dfs.finish_times)



