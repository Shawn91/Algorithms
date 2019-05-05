def insertion_sort(l):
    for i in range(1, len(l)):
        insert(l, i, l[i])

def insert(l, pos, val):
    for i in reversed(range(pos)):
        if val>=l[i]: # 排序目标比左边的数字还大，则该目标无需进一步排序了
            break
        elif l[i]<=val<=l[i+1]:
            l[i], l[pos] = l[pos], l[i]
            break
        elif i==0:
            l.insert(0, l.pop(pos))
            break


if __name__ == '__main__':
    l = [2,1,23]
    insertion_sort(l)
    print(l)
