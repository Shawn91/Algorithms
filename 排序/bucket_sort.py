import math

def bucket_sort(l, num_buckets=None):
    if num_buckets is None:
        num_buckets = len(l)
    max_val = max(l)
    min_val = min(l)
    bucket_size = (max_val - min_val + 1) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # 遍历元素，放入桶中
    for e in l:
        bucket_id = math.floor((e - min_val) / bucket_size)
        buckets[bucket_id].append(e)
    
    # 对每个桶内部排序; 应当使用 Insertion sort，因为每个桶内的元素数量不会太多，但此处为了方便，直接 sort
    for bucket in buckets:
        if bucket:
            bucket.sort()
    return [e for bucket in buckets for e in bucket]

if __name__ == '__main__':
    l = [1, 7, 9, 7, 8, 5, 4, 10, 8, 3]
    print(bucket_sort(l))
