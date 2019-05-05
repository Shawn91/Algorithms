"""这是一个最简单的 hash-based 搜索。直接将 C 中的每个元素都添加到了 hash table 中。"""

# 主体框架
def build_hash_table(C, hash_table_size):
    H = [[] for _ in range(hash_table_size)] # 使用 list 代替 linked list，作为 hash table 的 bin
    for e in C:
        hash_value = hash_function(e, hash_table_size)
        H[hash_value].append(e)
    print(H)
    return H

def search(item, H):
    hash_value = hash_function(item, len(H))
    return item in H[hash_value]

# hash 函数
def hash_function(s, hash_table_size):
    """一个简单的将英文字符串 hash 的函数"""
    hash_value = 0
    for i,e in enumerate(s):
        hash_value += ord(e) * 31 ** (len(s)-i-1)
    return abs(hash_value) % hash_table_size

# 综合以上
def hash_search(C, hash_table_size, item):
    H = build_hash_table(C, hash_table_size)
    return search(item, H)

if __name__ == '__main__':
    print(hash_search(['haha','heh','pupu'], 2, 'hh'))