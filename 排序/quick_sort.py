from statistics import median

def find_pivot(l, start=None, end=None):
    """使用 median of three 方法返回 pivot 的 index"""
    if start is None:
        start = 0
    if end is None:
        end = len(l)
    first_ele = l[start]
    last_ele = l[end-1]
    middle_ele = l[start+(end-start)//2]
    candidates = [first_ele,middle_ele,last_ele]
    
    return l[start:end].index(median(candidates))+start

def partition_by_pivot(l, pivot_index, start=None, end=None):
    """将数组 l 按照 pivot_index 划分成两半，并调整 l 中非 pivot 元素的位置
    Args:
        l(list): 为了确保整个排序时 inplace 的，这里的 l 始终是原始要排序的数组
        pivot_index (int): l[start:end] 这一段数组中的 pivot 在 l 中的 index
        start(int) and end(int): 在递归排序过程中，选取 l 的哪一段进行排序
    Returns:
        new index of pivot in l[start:end]
    """
    if start is None:
        start = 0
    if end is None:
        end = len(l)
    if pivot_index>=end or pivot_index<start:
        raise Exception('pivot index out of range')
    if len(l[start:end])<2:
        raise Exception('length must be at least 2 for partition_by_pivot to work')
    
    i = start + 1
    j = len(l[start:end])-1 + start
    pivot = l[pivot_index]
    # 第一步：将 pivot 移到开头
    l[start], l[pivot_index] = l[pivot_index], l[start]
    # 第二步，不断对调 i 和 j 的元素
    while i < j:
        while l[j] > pivot and j > i:
            j -= 1
        while l[i] < pivot and i < j:
            i += 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    # 跳出 while 时，i 和 j 必然相等
    if l[i] < pivot:
        l[start],l[i] = l[i],l[start]
        return i
    else:
        l[start], l[i-1] = l[i-1], l[start]
    return i-1

def quick_sort(l, start=None, end=None):
    """对 l[start:end] 段进行排序，一开始时，start=0, end=len(l)"""
    if start is None:
        start = 0
    if end is None:
        end = len(l)
    # 终止排序的条件
    if len(l[start:end]) < 2:
        return
    
    pivot_index = find_pivot(l, start=start, end=end)
    pivot_index = partition_by_pivot(l, pivot_index, start=start, end=end)
    start_left = start
    end_left = pivot_index
    start_right = pivot_index + 1
    end_right = end
    
    quick_sort(l, start=start_left, end=end_left)
    quick_sort(l, start=start_right, end=end_right)

if __name__ == '__main__':
    l = [1, 7, 9, 7, 8, 5, 4, 10, 8, 3]
    quick_sort(l)
    print(l)
