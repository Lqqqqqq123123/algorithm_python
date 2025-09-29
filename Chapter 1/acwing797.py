import sys
input = sys.stdin.readline
n, m = map(int, input().split())

d = [0] * (n + 10)

d[1:] = list(map(int, input().split()))

for i in range(m):
    l, r, c = map(int, input().split())
    d[l] += c; d[r + 1] -= c

for i in range(1, n + 1):
    d[i] += d[i - 1]

print(*d[1:n + 1])