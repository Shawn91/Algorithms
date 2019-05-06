"""假设已经有一些 hash 函数"""

class BloomFilter:
    def __init__(self, bit_array_size=1000, hash_functions=None):
        self.hash_functions = hash_functions
        self.bit_array_size = bit_array_size
        self.bit_array = [0 for _ in range(bit_array_size)] # list 模拟 bit array

    def add(self, e):
        """添加元素"""
        for hf in self.hash_functions:
            bit_array_index = hf(e)
            self.bit_array[bit_array_index] = 1

    def __contains__(self, item):
        for hf in self.hash_functions:
            if hf(item) == 0:
                return False
        return True # 包含。可能是 false positive 