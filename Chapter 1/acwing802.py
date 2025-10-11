# 排序+去重 sorted(set(arr))
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

adds = [(0, 0)] * n
queries = [(0, 0)] * m
alls = list()

for i in range(n):
    adds[i] = list(map(int, input().split()))
    alls.append(adds[i][0])

for i in range(m):
    queries[i] = list(map(int, input().split()))
    alls.append(queries[i][0] - 1); alls.append(queries[i][1])

alls = sorted(set(alls))

def find(x : int) -> int:
    l, r = 0, len(alls) - 1
    while l < r:
        mid = (l + r) >> 1
        if alls[mid] >= x: r = mid
        else: l = mid + 1
    
    return l + 1


a = [0] * (len(alls) + 1)

for i in range(n):
    a[find(adds[i][0])] += adds[i][1]

for i in range(1, len(alls) + 1):
    a[i] += a[i - 1]

for i in range(m): 
    print(a[find(queries[i][1])] - a[find(queries[i][0]) - 1])