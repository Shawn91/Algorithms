import math

def merge_sort(l, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(l)
    
    # 终止排序
    if end - start < 2: # 数组太小，不用排序
        return
    if end - start == 2: # 只剩两个元素时，按需调换元素顺序
        if l[end-1] < l[start]:
            l[start], l[end-1] = l[end-1], l[start]
        return
    
    # 递归排序
    mid = start + (end-start) // 2
    start_left = start
    end_left = mid
    start_right = mid
    end_right = end
    merge_sort(l, start=start_left, end=end_left)
    merge_sort(l, start=start_right, end=end_right)

    # 合并排序后的小数组
    copied_array = l[start:end]
    i = start # 左侧数组遍历用下标
    j = mid # 右侧数组遍历用下标
    k = 0 # 复制出的数组的遍历下标
    while k < end-start:
        if j>=end or (i < mid and l[i] < l[j]):
            copied_array[k] = l[i]
            i += 1
        else:
            copied_array[k] = l[j]
            j += 1
        k += 1
    
    # 复制出的数组经过更新后，替换原数组
    for i,val in enumerate(copied_array):
        l[start+i] = val

if __name__ == '__main__':
    l = [1, 7, 9, 7, 8, 5, 4, 10, 8, 3]
    merge_sort(l)
    print(l)
