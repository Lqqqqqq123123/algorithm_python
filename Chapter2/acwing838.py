import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline
prt = sys.stdout.write


import heapq

n, m = map(int, input().split())

arr = list(map(int, input().split()))
h = []
for x in arr:
    heapq.heappush(h, x)

for i in range(m):
    prt(str(heapq.heappop(h)) + ' ')