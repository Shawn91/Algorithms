class Node:
    def __init__(self, val=None):
        """创建一个 node"""
        self.value = val
        self.left = None
        self.right = None

    def add(self, val):
        """增加一个子 node"""
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)
class Tree:
    def __init__(self):
        """创建一个空 BST"""
        self.root = None

    def add(self, val):
        if self.root:
            self.root.add(val)
        else:
            self.root = Node(val)

    def __contains__(self, item):
        """根据 item 与树中节点大小的比较遍历 Tree 的部分 branches，判断 item 是否在树中"""
        node = self.root
        while node:
            if item < node.value:
                node = node.left
            elif item > node.value:
                node = node.right
            else:
                return True
        return False

if __name__ == '__main__':
    C = [1,2,3,4,5,6]
    t = Tree()
    for c in C:
        t.add(c)
    print(7 in t)