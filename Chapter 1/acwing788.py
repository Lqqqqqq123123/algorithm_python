# 788. 逆序对的数量-->归并排序练习
# 辅助数组
temp = list()

def merge_sort(arr, l, r):
    if l >= r: return 0

    mid = (l + r) >> 1
    res = merge_sort(arr, l, mid) + merge_sort(arr, mid + 1, r)
    i, j, k = l, mid + 1, 0

    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]; i += 1
        else: 
            temp[k] = arr[j]; j += 1
            res += (mid - i + 1)
        k += 1

    while i <= mid:
        temp[k] = arr[i]; i += 1; k += 1
    while j <= r:
        temp[k] = arr[j]; j += 1; k += 1
    
    arr[l:r + 1] = temp[:k]
    return res

import sys
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    temp = [0] * n
    arr = list(map(int, input().split()))
    print(merge_sort(arr, 0, n - 1))
    
