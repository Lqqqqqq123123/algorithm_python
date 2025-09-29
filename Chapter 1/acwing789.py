# 二分模板题
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = map(int, input().split())

while q:
    q -= 1
    x = int(input().strip())
    l, r = 0, n - 1
    r1, r2 = -1, -1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x : l = mid + 1
        else : r = mid
    if arr[l] == x : r1 = l

    l, r = 0, n - 1
    while l < r:
        mid = (l + r + 1) >> 1
        if arr[mid] <= x : l = mid
        else : r = mid - 1
    if arr[l] == x : r2 = l
    print(r1, r2)
