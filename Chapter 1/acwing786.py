import sys
input = sys.stdin.readline

def kth_num(arr, l, r, k) -> int:
    if l == r:
        return arr[l]

    i, j, pivot = l - 1, r + 1, arr[(l + r) >> 1]

    while i < j:
        i, j = i + 1, j - 1
        while arr[i] < pivot : i += 1
        while arr[j] > pivot : j -= 1
        if i < j: arr[i], arr[j] = arr[j], arr[i]

    if k <= (j - l + 1):
        return kth_num(arr, l, j, k)
    else :
        return kth_num(arr, j + 1, r, k - (j - l + 1))



if __name__ == '__main__':
    arr = list()
    n, k = map(int, input().split())
    arr.extend(list(map(int, input().split())))
    print(kth_num(arr, 0, len(arr) - 1, k))