"""使用 open addressing hash table 实现 hash table 中每个 bin 最多只储存一个元素时的搜索。
需要考虑 hash table 创建好后，又增删元素的情况
"""

class OpenAddressingHashTable:
    def __init__(self, hash_table_size):
        # 创建空 hash table
        self.hash_table = [None for _ in range(hash_table_size)]
        # 标记某个 bin 是否曾经有值又被删除（True 表示是）
        self.deleted = [False for _ in range(hash_table_size)]

    def add(self, e):
        """添加元素至 hash table 中"""
        hash_value = hash_function(e, len(self.hash_table)) % len(self.hash_table) # 使用 Python 自带的 hash 函数
        i = 0 # linear probing 公式中的 i，表示已经 probe 了多少次
        while self.hash_table[hash_value] is not None:
            if i == len(self.hash_table):
                raise Exception('probing failed')
            hash_value = self.probe(hash_value, i=i)
            i += 1
        self.hash_table[hash_value] = e
        if self.deleted[hash_value]:
            self.deleted[hash_value] = False

    # 使用 Linear probing
    def probe(self,hash_value, i=0,c=1):
        return (hash_value + c*i) % len(self.hash_table)

    def search(self, item):
        hash_value = hash_function(item, len(self.hash_table)) % len(self.hash_table)
        i = 0
        while self.hash_table[hash_value] is not None or self.deleted[hash_value]:
            if item == self.hash_table[hash_value]:
                return hash_value
            if i == len(self.hash_table):
                return -1 # 未找到
            hash_value = self.probe(hash_value, i=i)
            i += 1
        return -1

    def delete(self, e):
        index = self.search(e)
        if index != -1:
            self.hash_table[index] = None
            self.deleted[index] = True


    def __repr__(self):
        return str(self.hash_table)

# hash 函数
def hash_function(s, hash_table_size):
    """一个简单的将英文字符串 hash 的函数"""
    hash_value = 0
    for i,e in enumerate(s):
        hash_value += ord(e) * 31 ** (len(s)-i-1)
    return abs(hash_value) % hash_table_size


if __name__ == '__main__':
    C = ['A','B','C','B']
    ht = OpenAddressingHashTable(4)
    for e in C:
        ht.add(e)
    print(ht)
    ht.delete('B')
    print(ht)
    print(ht.search('B'))